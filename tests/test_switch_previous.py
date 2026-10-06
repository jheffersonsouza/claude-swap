"""Tests for `cswap switch -`, which rolls back to the previous account."""

import json
from pathlib import Path

from claude_swap.models import Platform
from claude_swap.switcher import ClaudeAccountSwitcher


def _switcher() -> ClaudeAccountSwitcher:
    s = ClaudeAccountSwitcher()
    s.platform = Platform.LINUX
    s._setup_directories()
    s._init_sequence_file()
    return s


def _creds(num: int) -> str:
    return json.dumps({
        "claudeAiOauth": {"accessToken": f"sk-{num}", "refreshToken": f"rt-{num}"},
    })


def _config(num: int, email: str) -> str:
    return json.dumps({
        "oauthAccount": {"emailAddress": email, "accountUuid": f"uuid-{num}"},
    })


def _add(s: ClaudeAccountSwitcher, num: int, email: str) -> None:
    """Store account `num` with credential and config backups."""
    s._write_account_credentials(str(num), email, _creds(num))
    s._write_account_config(str(num), email, _config(num, email))
    data = s._get_sequence_data()
    data["accounts"][str(num)] = {
        "email": email,
        "uuid": f"uuid-{num}",
        "organizationUuid": "",
        "organizationName": "",
        "added": "2024-01-01T00:00:00Z",
    }
    data["sequence"] = sorted({*data["sequence"], num})
    if data["activeAccountNumber"] is None:
        data["activeAccountNumber"] = num
    s._write_json(s.sequence_file, data)


def _log_in(home: Path, num: int, email: str) -> None:
    """Make `email` the live Claude Code login."""
    (home / ".claude" / ".credentials.json").write_text(_creds(num))
    (home / ".claude.json").write_text(_config(num, email))


def _live_email(home: Path) -> str:
    config = json.loads((home / ".claude.json").read_text())
    return config["oauthAccount"]["emailAddress"]


class TestSwitchToPrevious:
    def test_dash_rolls_back_to_the_previous_account(self, temp_home: Path):
        s = _switcher()
        _add(s, 1, "a@example.com")
        _add(s, 2, "b@example.com")
        _log_in(temp_home, 1, "a@example.com")
        s.switch_to("2", json_output=True)

        s.switch_to("-", json_output=True)

        assert _live_email(temp_home) == "a@example.com"
