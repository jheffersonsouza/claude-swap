"""Tests for the fork-only ``cs``/``cr`` shortcuts in ``shell/shortcuts.bash``.

Each case sources the file in bash, calls a shortcut, and records the argv a
fake ``cswap`` on PATH receives, one argument per line.
"""

from __future__ import annotations

import os
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

SHORTCUTS = Path(__file__).resolve().parents[1] / "shell" / "shortcuts.bash"

pytestmark = pytest.mark.skipif(
    sys.platform == "win32" or shutil.which("bash") is None,
    reason="the shortcuts are bash functions",
)


@pytest.fixture
def cswap_argv(tmp_path: Path):
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    fake = bin_dir / "cswap"
    fake.write_text('#!/bin/sh\nfor arg in "$@"; do printf "%s\\n" "$arg"; done\n')
    fake.chmod(0o755)

    def run(*words: str) -> list[str]:
        script = f"source {shlex.quote(str(SHORTCUTS))}; {shlex.join(words)}"
        env = {**os.environ, "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}"}
        result = subprocess.run(
            ["bash", "-c", script], env=env, capture_output=True, text=True, check=True
        )
        return result.stdout.splitlines()

    return run


class TestCs:
    def test_alone_opens_the_dashboard(self, cswap_argv):
        assert cswap_argv("cs") == []

    @pytest.mark.parametrize("account", ["3", "12", "user@example.com"])
    def test_account_switches(self, cswap_argv, account):
        assert cswap_argv("cs", account) == ["switch", account]

    def test_dash_rolls_back_to_the_previous_account(self, cswap_argv):
        assert cswap_argv("cs", "-") == ["switch", "-"]

    @pytest.mark.parametrize(
        "words",
        [("status",), ("list", "--token-status"), ("add",), ("switch", "dev")],
    )
    def test_other_commands_pass_through(self, cswap_argv, words):
        assert cswap_argv("cs", *words) == list(words)


class TestCr:
    SHARE = ["--share-history", "--share-plugins"]

    def test_alone_runs_the_mapped_account(self, cswap_argv):
        assert cswap_argv("cr") == ["run", *self.SHARE]

    def test_account_runs_with_shared_sessions_and_plugins(self, cswap_argv):
        assert cswap_argv("cr", "2") == ["run", "2", *self.SHARE, "--"]

    def test_claude_args_follow_the_separator(self, cswap_argv):
        assert cswap_argv("cr", "2", "--resume") == [
            "run", "2", *self.SHARE, "--", "--resume",
        ]

    def test_a_prompt_with_spaces_stays_one_argument(self, cswap_argv):
        assert cswap_argv("cr", "10", "Explique este arquivo") == [
            "run", "10", *self.SHARE, "--", "Explique este arquivo",
        ]
