# Trial the fork on this machine

Status: ready-for-human

## What to do

Install the fork from this checkout and use it with real Accounts for a day.

1. Run `uv tool install --editable .`, then `cswap help`.
2. For each Account, `/login` in Claude Code, then run `cswap add`. Never `/logout` first: it can revoke the refresh token of the Account being left. Check the result with `cswap list`.
3. Hot Swap: with an Instance running, run `cswap switch N` from another terminal. In the running Instance, `/status` should show the new Account, and the next message should go through without a restart.
4. Parallel Instance: run `cswap run N --share-history -- --resume`. Check that Sessions from the other Accounts are listed, and note what is missing (plugins, MCP server logins).
5. After a day, run `cswap list --token-status` and confirm no Account lost its login.

Record what worked, what broke, and which of the other issues still matter under `## Comments`.
