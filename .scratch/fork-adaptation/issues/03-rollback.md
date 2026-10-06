# Rollback to the previous Account in one step

Status: needs-triage

## Problem

After `cswap switch 3`, getting back requires the previous Account's number. The original brief wanted a one-step Rollback (`cs undo`).

## Options

- Shell side: `cs` records the active Account before each Swap, and `cs undo` Swaps back to it.
- Fork side: `cswap switch -` (like `cd -`), backed by a "previous Account" that claude-swap records on every Swap.

As of 2026-10-05, no upstream PR covers this.
