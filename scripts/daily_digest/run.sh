#!/usr/bin/env bash
# Daily 한미암 paper digest — runs at 10am via cron on ubuntu-d1.
#
# Phase B: search PubMed for new papers, download full PDFs, extract text,
# hand to claude CLI for relevance judgment + summary + Slack post.
# Phase A fallback: if no new candidates, post 2 from wiki backlog.
#
# Usage:
#   bash scripts/daily_digest/run.sh                 # normal run
#   DRY_RUN=1 bash scripts/daily_digest/run.sh       # search/download but don't post
#   DIGEST_DAYS=14 bash scripts/daily_digest/run.sh  # widen PubMed window
#   PHASE=A bash scripts/daily_digest/run.sh         # force backlog mode

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$REPO_ROOT"

LOG_DIR="$REPO_ROOT/logs"
mkdir -p "$LOG_DIR"
TODAY="$(date +%F)"
LOG_FILE="$LOG_DIR/digest-$TODAY.log"

# STAGE controls split-stage flow for exact 10:00:00 Slack delivery:
#   compose — runs the Claude pipeline but writes the draft message to /tmp
#             instead of posting (no slack MCP). Wiki/sources committed.
#   post    — reads draft, sleeps until 10:00:00, POSTs via Slack Web API,
#             updates slack-posted.json, commits.
#   full    — (default) original single-run behavior; Claude composes AND posts.
STAGE="${STAGE:-full}"
MSG_FILE="/tmp/digest_slack_msg_$TODAY.json"
SLACK_CHANNEL="C0B2RQ97Y3U"

exec > >(tee -a "$LOG_FILE") 2>&1

echo "================================================================"
echo "Daily digest run @ $(date -Iseconds) [STAGE=$STAGE]"
echo "Repo: $REPO_ROOT"
echo "================================================================"

# ============================================================
# STAGE=post — skip prep entirely; read pre-composed draft and
# fire it at Slack at exactly 10:00:00. No Claude call.
# ============================================================
if [ "$STAGE" = "post" ]; then
    if [ ! -f "$MSG_FILE" ]; then
        echo "ERROR: no draft message at $MSG_FILE — compose stage must run first."
        exit 1
    fi
    if [ -f "$MSG_FILE.posted" ]; then
        echo "INFO: $MSG_FILE.posted exists — already posted today. Exiting."
        exit 0
    fi
    if [ -z "${SLACK_BOT_TOKEN:-}" ]; then
        echo "ERROR: SLACK_BOT_TOKEN not set (expected from ~/.paperatlas.env via cron_entry.sh)."
        exit 1
    fi

    # Sleep until 10:00:00 local time, but only if the target is in a sane window
    # (don't sleep more than 10 min — protects against weird cron firings).
    TARGET_EPOCH=$(date -d "$(date +%F) 10:00:00" +%s)
    NOW_EPOCH=$(date +%s)
    SLEEP_SECS=$((TARGET_EPOCH - NOW_EPOCH))
    if [ "$SLEEP_SECS" -gt 0 ] && [ "$SLEEP_SECS" -le 600 ]; then
        echo "[post] sleeping ${SLEEP_SECS}s until 10:00:00 ($(date -d "@$TARGET_EPOCH" -Iseconds))..."
        sleep "$SLEEP_SECS"
    elif [ "$SLEEP_SECS" -le 0 ]; then
        echo "[post] 10:00:00 already passed ($((-SLEEP_SECS))s ago) — posting immediately."
    else
        echo "[post] WARN: target 10:00:00 is ${SLEEP_SECS}s away (too far) — posting immediately."
    fi

    echo "[post] firing at $(date -Iseconds)"

    # Build payload (use python so the message text — Korean, asterisks, newlines —
    # is encoded properly as JSON without shell-quoting headaches).
    PAYLOAD=$(python3 -c "
import json
m = json.load(open('$MSG_FILE'))
print(json.dumps({'channel': m['channel'], 'text': m['text']}, ensure_ascii=False))
")

    RESPONSE=$(curl -sS -X POST https://slack.com/api/chat.postMessage \
        -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "$PAYLOAD")

    OK=$(echo "$RESPONSE" | python3 -c "import json,sys; d=json.load(sys.stdin); print('yes' if d.get('ok') else 'no')" 2>/dev/null || echo "no")
    if [ "$OK" != "yes" ]; then
        echo "ERROR: Slack post failed. Response: $RESPONSE"
        exit 2
    fi
    SLACK_TS=$(echo "$RESPONSE" | python3 -c "import json,sys; print(json.load(sys.stdin).get('ts',''))")
    echo "[post] OK. ts=$SLACK_TS"

    # Update slack-posted.json (atomically) before marking the draft as posted,
    # so a crash between the two leaves us recoverable.
    STATE_TS="$SLACK_TS" STATE_DATE="$TODAY" STATE_MSG_FILE="$MSG_FILE" python3 - <<'PY'
import json, os
ts_str = os.environ['STATE_TS']
date = os.environ['STATE_DATE']
msg = json.load(open(os.environ['STATE_MSG_FILE']))
state_path = 'wiki/_meta/slack-posted.json'
state = json.load(open(state_path))
state.setdefault('pmids', [])
state.setdefault('slugs', [])
state.setdefault('history', [])
posted = []
pmids = msg.get('pmids', []) or []
slugs = msg.get('slugs', []) or []
for p, s in zip(pmids, slugs):
    if p and p not in state['pmids']:
        state['pmids'].append(p)
    if s and s not in state['slugs']:
        state['slugs'].append(s)
    posted.append({'slug': s, 'pmid': p})
state['history'].append({
    'date': date,
    'version': 'split-stage-v1',
    'ts': ts_str,
    'posted': posted,
})
with open(state_path, 'w') as f:
    json.dump(state, f, ensure_ascii=False, indent=2)
print(f'    Updated slack-posted.json (+{len(posted)} entries)')
PY

    mv "$MSG_FILE" "$MSG_FILE.posted"

    git add wiki/_meta/slack-posted.json wiki/sources/ 2>/dev/null || true
    if ! git diff --cached --quiet; then
        git -c user.email="paper-digest-bot@noreply" -c user.name="paper-digest-bot" \
            commit -m "Daily digest: posted $TODAY" --quiet
        git push --quiet origin main || echo "WARN: push failed; will retry tomorrow"
        echo "    Committed and pushed."
    else
        echo "    No state changes to commit."
    fi

    echo "================================================================"
    echo "Done @ $(date -Iseconds) [STAGE=post]"
    echo "================================================================"
    exit 0
fi

# Step 1: sync latest wiki (use rebase + autostash to handle local commits
# created by previous runs gracefully)
echo "[1/5] Pulling latest wiki..."
git pull --quiet --rebase --autostash origin main || {
    echo "WARN: rebase pull failed; trying merge"
    git pull --quiet --no-rebase origin main || echo "WARN: pull still failed; continuing with current local state"
}

# Step 2: PubMed monitor (Phase B), unless forced to Phase A
PHASE="${PHASE:-auto}"
DAYS="${DIGEST_DAYS:-7}"
PHASE_B_JSON="/tmp/digest_phaseb_$TODAY.json"
PHASE_A_JSON="/tmp/digest_phasea_$TODAY.json"
COMBINED="/tmp/digest_combined_$TODAY.json"
STANDARD_PATH="/tmp/digest_today.json"

if [ "$PHASE" = "A" ]; then
    echo "[2/5] PHASE=A forced; skipping PubMed search."
    PHASE_B_COUNT=0
else
    echo "[2/5] PubMed search (window=$DAYS days)..."
    # stdout = JSON, stderr = progress log → captured separately
    set +e
    python3 scripts/daily_digest/fetch_new_papers.py --days "$DAYS" \
        > "$PHASE_B_JSON" 2> "$LOG_DIR/phaseb-$TODAY.stderr"
    FETCH_RC=$?
    set -e
    cat "$LOG_DIR/phaseb-$TODAY.stderr"
    if [ "$FETCH_RC" -ne 0 ]; then
        echo "WARN: fetch_new_papers returned $FETCH_RC; treating as no candidates"
        echo '{"candidates":[],"date":"'$TODAY'","note":"fetch failed"}' > "$PHASE_B_JSON"
    fi
    PHASE_B_COUNT=$(python3 -c "import json; print(len(json.load(open('$PHASE_B_JSON')).get('candidates', [])))" 2>/dev/null || echo 0)
    echo "    Phase B: $PHASE_B_COUNT candidates with full PDF text"
fi

# Step 3: build combined input for claude
echo "[3/5] Preparing input for claude..."
if [ "$PHASE_B_COUNT" -gt 0 ]; then
    # Phase B has candidates → use them
    python3 -c "
import json
phaseb = json.load(open('$PHASE_B_JSON'))
out = {'mode': 'phase_b', 'date': phaseb['date'],
       'candidates': phaseb['candidates'],
       'esearch_count': phaseb.get('esearch_count', 0),
       'after_filter': phaseb.get('after_filter', 0)}
json.dump(out, open('$COMBINED', 'w'), ensure_ascii=False, indent=2)
"
    echo "    Mode: phase_b ($PHASE_B_COUNT candidates)"
else
    # Fallback: pick from backlog
    echo "    No fresh PubMed candidates; falling back to backlog"
    python3 scripts/daily_digest/select_papers.py > "$PHASE_A_JSON"
    SEL_COUNT=$(python3 -c "import json; print(len(json.load(open('$PHASE_A_JSON'))['selected']))")
    if [ "$SEL_COUNT" -lt 2 ]; then
        echo "ERROR: backlog also exhausted (only $SEL_COUNT papers). Aborting."
        exit 1
    fi
    python3 -c "
import json
phasea = json.load(open('$PHASE_A_JSON'))
out = {'mode': 'phase_a_fallback', 'date': phasea['date'],
       'selected': phasea['selected'], 'candidates': []}
json.dump(out, open('$COMBINED', 'w'), ensure_ascii=False, indent=2)
"
    echo "    Mode: phase_a_fallback ($SEL_COUNT backlog papers)"
fi

# Quick summary for log
python3 -c "
import json
d = json.load(open('$COMBINED'))
print(f'    Mode: {d[\"mode\"]}, Date: {d[\"date\"]}')
if d['mode'] == 'phase_b':
    for i, c in enumerate(d['candidates'], 1):
        print(f'      Phase B #{i}: PMID {c[\"pmid\"]} — {c[\"journal\"][:40]} — {c[\"title\"][:60]}...')
else:
    for i, s in enumerate(d['selected'], 1):
        print(f'      Phase A #{i}: {s[\"slug\"][:60]}')
"

if [ "${DRY_RUN:-0}" = "1" ]; then
    echo "[DRY_RUN=1] Stopping before Slack post."
    echo "Combined input written to: $COMBINED"
    exit 0
fi

# Symlink so claude (and prompt.md) can read from a stable path
rm -f "$STANDARD_PATH"
ln -s "$COMBINED" "$STANDARD_PATH"

# Step 4: hand to claude
PROMPT_FILE="$REPO_ROOT/scripts/daily_digest/prompt.md"
CONTEXT_FILE="$REPO_ROOT/wiki/_meta/han-mi-am-project-context.md"

if [ "$STAGE" = "compose" ]; then
    echo "[4/5] Composing draft via claude (DRAFT mode — no Slack post)..."
    DRAFT_OVERRIDE='

---

## RUNTIME OVERRIDE — DRAFT MODE (split-stage flow)

**You are running in DRAFT mode. Do NOT call any slack MCP tool — it is not in your allowed tool list.**

Replace step 4 (Post to Slack) with this:
- Use the Write tool to save a JSON file at `'"$MSG_FILE"'` with this exact shape:
  ```json
  {"channel": "'"$SLACK_CHANNEL"'", "text": "<the final composed Slack message text, exactly as you would have posted>", "pmids": ["<pmid1>","<pmid2>"], "slugs": ["<slug1>","<slug2>"]}
  ```
- The `text` field must be the EXACT message body (Korean composition, all `*bold*`, all `\n` newlines, all hyperlinks) that you would have sent to Slack. The post stage will pipe it verbatim into `chat.postMessage`.

**Skip step 6 (Update slack-posted.json) entirely.** That happens at the actual post step, not here. Step 5 (wiki/sources updates) proceeds as normal.

When finished, print a one-line summary:
```
DRAFT: composed message for N papers (pmids: ...). Saved to '"$MSG_FILE"'
```
'
    claude -p "$(cat "$PROMPT_FILE")$DRAFT_OVERRIDE" \
        --append-system-prompt "$(cat "$CONTEXT_FILE")" \
        --allowed-tools "Read,Edit,Write,Bash" \
        || {
            echo "ERROR: claude (compose) failed (exit $?)"
            exit 2
        }

    if [ ! -f "$MSG_FILE" ]; then
        echo "ERROR: compose finished but $MSG_FILE was not created."
        exit 3
    fi

    echo "[5/5] Committing wiki/sources (slack-posted.json deferred to post stage)..."
    git add wiki/sources/ 2>/dev/null || true
    if ! git diff --cached --quiet; then
        git -c user.email="paper-digest-bot@noreply" -c user.name="paper-digest-bot" \
            commit -m "Daily digest: draft sources for $TODAY" --quiet
        git push --quiet origin main || echo "WARN: push failed"
        echo "    Committed wiki/sources."
    else
        echo "    No wiki/sources changes."
    fi

    echo "================================================================"
    echo "Compose done @ $(date -Iseconds). Draft ready at $MSG_FILE"
    echo "================================================================"
    exit 0
fi

# STAGE=full — original single-run behavior (compose + post via Claude+Slack MCP)
echo "[4/5] Posting to Slack via claude + slack MCP..."
claude -p "$(cat "$PROMPT_FILE")" \
    --append-system-prompt "$(cat "$CONTEXT_FILE")" \
    --allowed-tools "Read,Edit,Write,Bash,mcp__slack" \
    || {
        echo "ERROR: claude run failed (exit $?)"
        exit 2
    }

# Step 5: commit any state changes
echo "[5/5] Committing wiki state..."
git add wiki/_meta/slack-posted.json wiki/sources/ 2>/dev/null || true
if ! git diff --cached --quiet; then
    git -c user.email="paper-digest-bot@noreply" -c user.name="paper-digest-bot" \
        commit -m "Daily digest: posted $TODAY" --quiet
    git push --quiet origin main || echo "WARN: push failed; will retry tomorrow"
    echo "    Committed and pushed."
else
    echo "    No state changes to commit (nothing posted?)"
fi

echo "================================================================"
echo "Done @ $(date -Iseconds)"
echo "================================================================"
