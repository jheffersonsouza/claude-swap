# Plugins in Parallel Instances

Status: needs-triage

## Problem

`cswap run` shares `settings.json`, `CLAUDE.md`, skills, commands and agents, but it deliberately leaves `plugins/` out (`SHARED_ITEMS` in `src/claude_swap/session.py`). `settings.json` still lists the enabled plugins, so a Parallel Instance points at plugins its Profile doesn't have. Upstream request: realiti4/claude-swap#304.

## To find out

- Why upstream treats `plugins/` as Account- or Instance-scoped.
- Whether linking `plugins/`, or part of it, into a Parallel Instance's Profile is safe.
