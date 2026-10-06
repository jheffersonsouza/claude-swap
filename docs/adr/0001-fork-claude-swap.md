# Fork claude-swap instead of building a new tool

We need several Claude Code Accounts on one Linux machine, side by side and swappable under running work. claude-swap already does this:

- It Swaps the Default Profile's Account while Instances keep running, because Claude Code reloads its credential file when the file changes.
- It runs Parallel Instances with `cswap run`.
- It keeps MCP server logins with the Profile.

So we fork it and keep our changes small, instead of building the planned `cr`/`cs` tool from scratch, and upstream fixes keep flowing in.

## Considered Options

- **Build our own tool** (shell or Bun): rejected. claude-swap already solves the hard parts: Claude Code's credential locks, refresh-token rotation, and which credential keys belong to the Account and which to the Profile.
- **caam** (Dicklesworthstone/coding_agent_account_manager): a generic token backup and restore tool for several coding CLIs, under a custom license, and less Claude-specific.
- **Profile wrappers over `CLAUDE_CONFIG_DIR`** (claude-rig, silo, claudenv and others): isolation-first, with no Hot Swap.

## Consequences

- Upstream gaps become our work:
  - Plugins and MCP server logins don't follow Parallel Instances.
  - Sessions are shared only with `--share-history`.
  - There is no one-step Rollback.
- Open upstream bugs can destroy a stored refresh token (realiti4/claude-swap#383, #381). Watch them before relying on auto-switch.
