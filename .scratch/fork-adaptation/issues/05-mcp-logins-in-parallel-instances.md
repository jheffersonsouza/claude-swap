# MCP server logins in Parallel Instances

Status: needs-triage

## Problem

`cswap run` mirrors user-scope `mcpServers` but not their OAuth logins, so each Parallel Instance's Profile asks for HTTP MCP server auth again (README, "Sharing details"). With one shared setup across Accounts, MCP server logins should follow every Profile.

## To find out

Whether copying or linking the Profile-owned credential keys (`mcpOAuth`, `mcpOAuthClientConfig`; `SHARED_CREDENTIAL_KEYS` in `src/claude_swap/credentials.py`) into Parallel Instance Profiles stays safe when those tokens rotate.

As of 2026-10-05, no upstream PR shares MCP server logins into Parallel Instance Profiles. #300 does the opposite (per-Account MCP servers), and #163 (`--share-all`) conflicts with main.
