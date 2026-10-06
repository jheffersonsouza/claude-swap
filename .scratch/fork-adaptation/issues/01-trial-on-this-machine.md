# Trial claude-swap on this machine

Status: ready-for-human

## Progress

2026-10-05:

- The fork is installed globally (0.27.0b1 plus the merged upstream PRs), and `~/.bashrc` loads `cs` and `cr`.
- Slot 1 is registered but needs a re-login, because its refresh token is dead.
- Slot 2 is active.
- Slot 3 is registered.

## What to do

1. For each Account that is missing or dead, `/login` in Claude Code, then run `cswap add`. On an existing slot, `add` refreshes it instead of duplicating it. Never `/logout` first: it can revoke the refresh token of the Account being left.
2. Hot Swap: with an Instance running, run `cswap switch N` from another terminal. In the running Instance, `/status` should show the new Account, and the next message should go through without a restart.
3. Parallel Instance: run `cr N --resume`. Check that Sessions and plugins from the other Accounts show up, and note what is missing (MCP server logins).
4. After a day, run `cswap list --token-status` and confirm no Account lost its login.

Record what worked, what broke, and which of the other issues still matter under `## Comments`.
