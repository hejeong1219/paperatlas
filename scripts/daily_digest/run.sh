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

exec > >(tee -a "$LOG_FILE") 2>&1

echo "================================================================"
echo "Daily digest run @ $(date -Iseconds)"
echo "Repo: $REPO_ROOT"
echo "================================================================"

# Step 1: sync latest wiki
echo "[1/5] Pulling latest wiki..."
git pull --quiet --ff-only origin main || echo "WARN: git pull failed"

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
echo "[4/5] Posting to Slack via claude + slack MCP..."
PROMPT_FILE="$REPO_ROOT/scripts/daily_digest/prompt.md"
CONTEXT_FILE="$REPO_ROOT/wiki/_meta/han-mi-am-project-context.md"

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
