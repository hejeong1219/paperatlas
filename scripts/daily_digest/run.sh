#!/usr/bin/env bash
# Daily 한미암 paper digest — runs at 10am via cron on ubuntu-d1.
#
# Pulls latest wiki, picks 2 backlog papers, hands them to `claude` CLI which
# uses the slack MCP to post to #한미암_관련논문 (C0B2RQ97Y3U).
#
# Usage:
#   bash scripts/daily_digest/run.sh           # normal run
#   DRY_RUN=1 bash scripts/daily_digest/run.sh # pick papers but don't post

set -euo pipefail

# Resolve repo root from this script's location
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$REPO_ROOT"

LOG_DIR="$REPO_ROOT/logs"
mkdir -p "$LOG_DIR"
TODAY="$(date +%F)"
LOG_FILE="$LOG_DIR/digest-$TODAY.log"

# Tee everything to log too
exec > >(tee -a "$LOG_FILE") 2>&1

echo "================================================================"
echo "Daily digest run @ $(date -Iseconds)"
echo "Repo: $REPO_ROOT"
echo "================================================================"

# Step 1: Sync latest wiki from GitHub (in case Mac pushed new sources today)
echo "[1/4] Pulling latest wiki..."
git pull --quiet --ff-only origin main || {
    echo "WARN: git pull failed; continuing with current local state"
}

# Step 2: Select 2 papers
echo "[2/4] Selecting papers..."
python3 scripts/daily_digest/select_papers.py > /tmp/digest_today.json
SELECTED_COUNT=$(python3 -c "import json; print(len(json.load(open('/tmp/digest_today.json'))['selected']))")
TOTAL_CAND=$(python3 -c "import json; print(json.load(open('/tmp/digest_today.json'))['total_candidates'])")
echo "    Selected $SELECTED_COUNT papers from $TOTAL_CAND candidates"
if [ "$SELECTED_COUNT" -lt 2 ]; then
    echo "ERROR: fewer than 2 papers selected. Backlog may be exhausted."
    exit 1
fi

# Show selection for log readability
python3 -c "
import json
d = json.load(open('/tmp/digest_today.json'))
for i, p in enumerate(d['selected'], 1):
    m = p['meta']
    print(f'  #{i} [{p[\"score\"]}] {m.get(\"year\", \"?\")} {m.get(\"journal\", \"?\")} — {p[\"slug\"]}')"

if [ "${DRY_RUN:-0}" = "1" ]; then
    echo "[DRY_RUN=1] Stopping before Slack post."
    cat /tmp/digest_today.json
    exit 0
fi

# Step 3: Hand to Claude CLI to format + post via Slack MCP
echo "[3/4] Posting to Slack via claude + slack MCP..."
PROMPT_FILE="$REPO_ROOT/scripts/daily_digest/prompt.md"
CONTEXT_FILE="$REPO_ROOT/wiki/_meta/han-mi-am-project-context.md"

# Pass: prompt as user message, project context as appended system prompt.
# `claude -p` runs in non-interactive mode and exits when done.
claude -p "$(cat "$PROMPT_FILE")" \
    --append-system-prompt "$(cat "$CONTEXT_FILE")" \
    --allowed-tools "Read,Edit,Write,Bash,mcp__slack" \
    || {
        echo "ERROR: claude run failed"
        exit 2
    }

# Step 4: Commit any changes (slack-posted.json + new wiki entries)
echo "[4/4] Committing wiki state..."
git add wiki/_meta/slack-posted.json 2>/dev/null || true
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
