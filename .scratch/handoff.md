# Handoff (2026-10-05)

For the next session, which starts with zero context. Delete this file once nothing in it is still needed.

## Where things stand

- This repo is the user's public fork of claude-swap: `origin` is jheffersonsouza/claude-swap, `upstream` is realiti4/claude-swap. For why, see `docs/adr/0001-fork-claude-swap.md`. For how to work here, see `CLAUDE.md`. The glossary is `CONTEXT.md`.
- `main` holds:
  - upstream main;
  - 7 upstream PRs merged ahead of upstream (`git log --merges --grep 'upstream pr'`);
  - the fork docs;
  - the `cs`/`cr` shortcuts in `shell/shortcuts.bash`.
- Nothing is pushed: `main` is 37 commits ahead of `origin/main`. Push only when the user asks.
- The global `cswap` is a snapshot of this fork's `main` (0.27.0b1), and `~/.bashrc` sources the shortcuts.
- Test baseline: `uv run pytest` gives 2401 passed and 3 skipped. It also shows 3 `PytestRemovedIn10Warning`s that predate us; upstream PR #389 fixes them.
- The cswap store has three Account slots:
  - Slot 1 needs a re-login: `/login` with that Account in Claude Code, then `cswap add`. Never `/logout` first.
  - Slot 2 was active at the last check.
  - Slot 3 is registered.

## Open work

All in `.scratch/fork-adaptation/issues/`:

- `01-trial-on-this-machine.md` (ready-for-human): the user tries Hot Swap and `cr` for a day and reports back.
- `03-rollback.md` (needs-triage): the user liked the idea and parked it. Preferred design: `cswap switch -` in the fork.
- `05-mcp-logins-in-parallel-instances.md` (needs-triage).

The user dropped the rate-limit and policy research on purpose. Don't reopen it unprompted.

## Working with this user

- Talk in PT-BR, short and direct. Write artifacts (code, docs, issues, commits) in English.
- Do one task at a time and report after each.
- Run no subagents or background agents unless the user asks. This rule is also in `CLAUDE.md` and in memory.
- Commit freely and never push. Use the user's `commit` skill: conventional, lowercase, no AI mentions, no Co-Authored-By.
- Delete a resolved issue rather than marking it closed, so `.scratch/` lists only what still needs doing.
- Before replacing files or running a command that changes Accounts, confirm with the user.

## Suggested skills

The agent calls these through the Skill tool:

- `commit`: every commit.
- `mattpocock-skills:tdd`: implementing rollback (`cswap switch -`) or any other fork change.
- `mattpocock-skills:codebase-design`: placing "previous Account" state in `switcher.py`.
- `mattpocock-skills:grilling` and `mattpocock-skills:domain-modeling`: settling MCP-login sharing (issue 05) and any new terms.
- `mattpocock-skills:diagnosing-bugs`: if the trial in issue 01 turns up a failure.
- `mattpocock-skills:code-review`: before merging a feature branch into `main`.
- `mattpocock-skills:pr`: writing a PR body if a change goes upstream.

The user types this one: `/mattpocock-skills:triage`, to move issues 03 and 05 out of needs-triage.
