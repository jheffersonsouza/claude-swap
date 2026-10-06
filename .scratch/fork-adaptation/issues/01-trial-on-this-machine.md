# Trial claude-swap on this machine

Status: ready-for-human

## Progress

2026-10-05:

- Upstream 0.26.0 is installed globally with `uv tool install claude-swap`.
- Slot 1 is registered but needs a re-login, because its refresh token is dead.
- Slot 2 is active.
- A third Account is not registered yet.

## What to do

1. For each Account that is missing or dead, `/login` in Claude Code, then run `cswap add`. On an existing slot, `add` refreshes it instead of duplicating it. Never `/logout` first: it can revoke the refresh token of the Account being left.
2. Hot Swap: with an Instance running, run `cswap switch N` from another terminal. In the running Instance, `/status` should show the new Account, and the next message should go through without a restart.
3. Parallel Instance: run `cswap run N --share-history -- --resume`. Check that Sessions from the other Accounts are listed, and note what is missing (plugins, MCP server logins). Don't run `cswap list` inside that terminal: upstream #433 reports it logging out every Instance on the slot.
4. After a day, run `cswap list --token-status` and confirm no Account lost its login.

Record what worked, what broke, and which of the other issues still matter under `## Comments`.
