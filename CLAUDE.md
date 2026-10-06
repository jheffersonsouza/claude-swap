# claude-swap (personal fork)

Fork of [realiti4/claude-swap](https://github.com/realiti4/claude-swap) (`cswap`), used to run several Claude Code Accounts on one Linux machine: side by side, and swapped under running work. Why a fork instead of a new tool: `docs/adr/0001-fork-claude-swap.md`. Remaining work: `.scratch/fork-adaptation/issues/`.

## Working here

- Daily use from this checkout: `uv tool install --editable .`; code changes apply on the next `cswap` run.
- Tests: `uv sync --locked`, then `uv run pytest` (same as `.github/workflows/ci.yml`).
- `upstream` is realiti4/claude-swap. Sync with `git fetch upstream && git merge upstream/main`.
- Fork-only files (`CLAUDE.md`, `CONTEXT.md`, `docs/agents/`, `docs/adr/`, `.scratch/`) stay off branches meant for upstream PRs; branch those from `upstream/main`.
- `cswap switch`, `add`, `remove`, `auto` and `import` rewrite the real `~/.claude` login: run them only with the user. Experiments use a throwaway `CLAUDE_CONFIG_DIR`, and Credential values are never printed.
- Work inline in the main session; spawn subagents only when the user asks, whatever a skill step says.

## Agent skills

### Issue tracker

Issues live as local markdown files under `.scratch/<feature-slug>/`. See `docs/agents/issue-tracker.md`.

### Triage labels

Default five-role vocabulary; each label string equals its role name. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: one `CONTEXT.md` and one `docs/adr/` at the repo root. See `docs/agents/domain.md`.
