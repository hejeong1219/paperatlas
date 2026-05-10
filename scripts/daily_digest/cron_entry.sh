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
# To install in crontab:
#   crontab -e
#   # add line (matches local timezone — d1 is KST):
#   0 10 * * * /home/hejeong/paperatlas/scripts/daily_digest/cron_entry.sh >> /home/hejeong/paperatlas/logs/cron-wrapper.log 2>&1

set -uo pipefail

# 1. Conda — try common install locations
for p in "$HOME/anaconda3" "$HOME/miniconda3" "$HOME/miniforge3" "/opt/anaconda3" "/opt/miniconda3"; do
    if [ -f "$p/etc/profile.d/conda.sh" ]; then
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

# 4. Run the digest
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$REPO_ROOT" || exit 1

# Default DIGEST_DAYS=7 (strict daily); override via env if needed
exec /usr/bin/env DIGEST_DAYS="${DIGEST_DAYS:-7}" bash "$SCRIPT_DIR/run.sh"
