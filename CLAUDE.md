# claude-swap (personal fork)

Fork of [realiti4/claude-swap](https://github.com/realiti4/claude-swap) (`cswap`), used to run several Claude Code Accounts on one Linux machine: side by side, and swapped under running work. Why a fork instead of a new tool: `docs/adr/0001-fork-claude-swap.md`. Remaining work: `.scratch/fork-adaptation/issues/`.

## Working here

- Daily use runs a snapshot of this fork, installed globally with `uv tool install .`. After merging into `main`, refresh it with `uv tool install . --reinstall`. Try work in progress with `uv run cswap ...`. Both share the account store in `~/.local/share/claude-swap/`; to keep a trial apart, point `XDG_DATA_HOME` at a temp dir.
- `~/.bashrc` sources `shell/shortcuts.bash` (`cs`, `cr`).
- Tests: `uv sync --locked`, then `uv run pytest` (same as `.github/workflows/ci.yml`).
- `upstream` is realiti4/claude-swap. Sync with `git fetch upstream && git merge upstream/main`. Some upstream PRs are merged here ahead of upstream (`git log --merges --grep 'upstream pr'`); if upstream later squash-merges one, keep upstream's version on conflict.
- Fork-only files (`CLAUDE.md`, `CONTEXT.md`, `docs/agents/`, `docs/adr/`, `.scratch/`, `shell/`, `tests/test_shell_shortcuts.py`) stay off branches meant for upstream PRs; branch those from `upstream/main`.
- `cswap switch`, `add`, `remove`, `auto` and `import` rewrite the real `~/.claude` login: run them only with the user. Experiments use a throwaway `CLAUDE_CONFIG_DIR`, and Credential values are never printed.
- Work inline in the main session; spawn subagents only when the user asks, whatever a skill step says.

## Agent skills

### Issue tracker

Issues live as local markdown files under `.scratch/<feature-slug>/`. See `docs/agents/issue-tracker.md`.

### Triage labels

Default five-role vocabulary; each label string equals its role name. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: one `CONTEXT.md` and one `docs/adr/` at the repo root. See `docs/agents/domain.md`.
