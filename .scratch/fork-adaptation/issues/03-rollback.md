# Rollback to the previous Account in one step

Status: needs-triage

## Problem

After `cswap switch 3`, getting back requires the previous Account's number. The original brief wanted a one-step Rollback (`cs undo`).

## Options

- Shell side: `cs` records the active Account before each Swap, and `cs -` Swaps back to it. Simple, but it only sees Swaps made through `cs`.
- Fork side: `cswap switch -` (like `cd -`), backed by a "previous Account" that claude-swap records on every Swap. This also sees Swaps from the dashboard, `cswap auto` and plain `cswap switch`, and could go upstream as a PR. Preferred.

As of 2026-10-05, no upstream PR covers this.
