# Merge useful upstream PRs into the fork

Status: ready-for-agent

## What to do

These open upstream PRs (realiti4/claude-swap) match this fork's needs. All were reported mergeable on 2026-10-05. Merge them one at a time on a branch, and run `uv run pytest` after each.

Sharing in Parallel Instances:

- #294 `--share-plugins`: links the plugin store into Parallel Instance Profiles. See [Plugins in Parallel Instances](04-plugins-in-parallel-instances.md).
- #223: `--share-history` no longer loses transcripts on collisions and races.
- #356: `--share-history` survives a corrupt or torn `history.jsonl`.
- #430: carries folder trust from the Default Profile into Parallel Instance Profiles.

Refresh-token safety (bugs present in 0.26.0):

- #384: stops two Swap paths that strand a slot's refresh token. Fixes #383.
- #433: `cswap list` inside a `cswap run` shell no longer rotates another Profile's tokens.
- #351: a slot whose Parallel Instance Profile holds a live token family is no longer quarantined.

Skipped: #163 (`cswap env`, `--share-all`) conflicts with main. Recheck it if [Shell shortcuts `cs` and `cr`](02-shell-shortcuts.md) or [MCP server logins in Parallel Instances](05-mcp-logins-in-parallel-instances.md) needs it.
