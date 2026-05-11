#!/usr/bin/env bash
# Cron entry point — wraps run.sh with the environment cron lacks by default.
#
# cron runs in a minimal shell with no conda, no .bashrc, restricted PATH.
# This wrapper:
#   1. Sources conda (so python3 + ml libs work)
#   2. Adds typical user-bin locations to PATH (so `claude`, `git`, `pdftotext` resolve)
#   3. Changes to repo root
#   4. Calls run.sh with default DIGEST_DAYS=7
#
# To install in crontab (weekly Wednesday flow for exact 10:00:00 Slack delivery):
#   crontab -e
#   # compose at 9:50 Wed (Claude drafts to /tmp), post at 9:59 Wed (sleeps until 10:00:00 exactly):
#   50 9 * * 3 STAGE=compose /home/hejeong/paperatlas/scripts/daily_digest/cron_entry.sh >> /home/hejeong/paperatlas/logs/cron-wrapper.log 2>&1
#   59 9 * * 3 STAGE=post    /home/hejeong/paperatlas/scripts/daily_digest/cron_entry.sh >> /home/hejeong/paperatlas/logs/cron-wrapper.log 2>&1
#
# (Single-run fallback, if you don't care about exact timing:
#   0 10 * * 3 /home/hejeong/paperatlas/scripts/daily_digest/cron_entry.sh >> ... )

set -o pipefail
# Note: do NOT enable `set -u` here — conda's profile.d/conda.sh references
# unset variables internally and would silently kill this wrapper.

# 1. Conda — try common install locations (the user's `(base)` prompt
# implies conda is active in their interactive shell; in cron we must
# load it explicitly).
for p in "$HOME/anaconda3" "$HOME/miniconda3" "$HOME/miniforge3" "/opt/anaconda3" "/opt/miniconda3" "/opt/conda"; do
    if [ -f "$p/etc/profile.d/conda.sh" ]; then
        echo "[cron_entry] sourcing conda from $p" >&2
        # shellcheck disable=SC1091
        source "$p/etc/profile.d/conda.sh"
        conda activate base 2>/dev/null || true
        break
    fi
done

# 2. PATH — claude CLI is typically in ~/.local/bin or /usr/local/bin
export PATH="$HOME/.local/bin:/usr/local/bin:/usr/bin:/bin:$PATH"

# 3. SSH key for git push (no passphrase key at default location)
export GIT_SSH_COMMAND="ssh -i $HOME/.ssh/id_ed25519 -o StrictHostKeyChecking=no"

# 4. Load Slack bot token (and any other secrets) from ~/.paperatlas.env if present.
# Not in git; chmod 600. Needed for STAGE=post (curl to Slack API).
if [ -f "$HOME/.paperatlas.env" ]; then
    # shellcheck disable=SC1091
    source "$HOME/.paperatlas.env"
fi

# 5. Run the digest
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$REPO_ROOT" || exit 1

echo "[cron_entry] launching run.sh from $REPO_ROOT (STAGE=${STAGE:-full}, DIGEST_DAYS=${DIGEST_DAYS:-14}, DRY_RUN=${DRY_RUN:-0})" >&2

# Default STAGE=full (original behavior). Override via env from crontab for split flow.
# DIGEST_DAYS=14 widens Entrez window so the strict proteogenomic query gets ~2-4 hits/run
# (slack-posted.json filter de-dupes across days, so reprocessing is fine).
DIGEST_DAYS="${DIGEST_DAYS:-14}" DRY_RUN="${DRY_RUN:-0}" STAGE="${STAGE:-full}" bash "$SCRIPT_DIR/run.sh"
