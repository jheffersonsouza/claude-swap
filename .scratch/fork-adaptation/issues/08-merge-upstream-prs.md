# Merge more upstream PRs

Status: needs-triage

## Context

On 2026-10-15, 50 of the 132 open upstream PRs (realiti4/claude-swap) that the fork does not carry yet were checked against `main` at 9135d0c (upstream 0.28.0b1). Each one was test-merged. The 29 that merge cleanly ran the test suite in a sandbox with no network and the home directory hidden. The other 82 were left out by title: macOS, Windows or menu bar only, API-key Accounts, large feature sets, or docs.

How the fork is used weighs in: Hot Swap of the Default Profile (`cs`), Parallel Instances through `cr`, three Accounts in one Team org, and no `cswap auto` so far.

## Merge

- #443: refuses to make an Account the Default Profile's login while a Parallel Instance of it runs, because one refresh token in two places logs one copy out. Also fixes #381: `cr N` run from inside another Parallel Instance spent the Default Profile's refresh token. Adds `cswap run N --own-login`. Conflicts with upstream 6145afd in `_perform_switch`: keep both of #443's refusals, then 6145afd's refusal for an adoption it cannot decide. Also pass `share_plugins` to `_sync_sharing` in the own-login branch of `setup_session`; git does not flag that one.
- #445: `cswap add` refuses a Credential that Claude Code wiped after `invalid_grant`, instead of overwriting the slot's backup with empty tokens. Fixes #444.
- #359: an undecodable `.enc` backup, the only backend on Linux, no longer crashes `cswap list`, `switch` and `auto`.
- #266: the lock heartbeat survives a transient error, lock waits honour their timeout, and stale-lock takeover is serialized. The upstream maintainer called it good and asked for small changes, which the author reports as done.
- #358: `cswap add --slot N`, the documented re-login path, keeps the slot's alias and disabled flag. Test-only conflict in `tests/test_switcher.py`: keep both blocks.

Merged together on a trial branch in that order, with the resolutions above, the suite passes three runs in a row: 2603 passed, 3 skipped.

## Optional

Each one merges cleanly and passes the suite unless noted.

- #307: a hollow usage reading (0%, no reset time) no longer overwrites a real cached one for an idle Account.
- #365: the duplicate-Account warning compares reset instants with a 5 s tolerance, so it can fire on real data.
- #424: a 403 for a lapsed plan shows its cause instead of `http-403`. Touches the same lines as #407 in `_classify_usage_error`.
- #407: a refused TLS certificate is reported apart from an unreachable host.
- #423: re-adding an Account keeps the stored organization name. Touches the same lines as #358 in `add_account`.
- #392: `cswap list` and the TUI show how long until each Account must log in again. 13 conflict hunks, most of them in the menu bar.
- #176: `cswap statusline` for Claude Code's status line. Inside a Parallel Instance it names that Instance's Account. 2 conflict hunks in `cli.py`.
- #175: a `.claude-account` file pins a directory's Account for `cswap run`. Its pin branch drops `--share-plugins` and `--require-session`, and one test fails on that; fix both if it is merged.
- #400: the TUI turns mouse reporting off over SSH.
- #284: retries an empty backup read once, a macOS Keychain symptom.

## Only with `cswap auto`

All of these merge cleanly and pass: #375 (respects a manual Swap for a set time), #432, #404, #449 (Team seats: rank by the model's weekly reset), #343, #379, #285 (desktop notifications), #253, #370.

## Only with Remote Control

- #446 reports the Instances a Swap disconnects from Remote Control. Test-only conflict.
- #417 adds `cswap rc`, which reconnects Remote Control after a Swap.
- #467 recovers attachments lost to a Swap.

## Skip

- #405: Credential provenance guards. Worth having, but it refuses backup writes nobody attributed, and the PRs already merged here add write paths it does not know about. Take it once upstream merges it.
- #268: temp files left behind by atomic writes. It conflicts with upstream's new `_write_json`; wait for upstream.
- #287: a rewrite of lock release. Very complex, and it conflicts with #266.
- #286: rollback of `cswap swap`. Large, and the fork does not use `swap`.
- #275, #213, #212, #166, #214, #243, #309, #409, #163, #386, #108: old, conflicting, superseded, or macOS only. #212's premise does not hold on Claude Code 2.1.301: `claude auth status` still reports `authMethod: claude.ai`.
- #401: refreshes the org-policy cache on a Swap, but all three Accounts share one org.
- #427: matters only when `sessions/` is symlinked across Profiles.
- #439: `cr` already passes `--share-history`.
- #338: Fable allocation for `cswap run --auto`. It clashes with #386 over the flag.
- #336: renumbers slots after a remove.
- #361: macOS only.
- #380: a design proposal with no code.
- #470: `cswap warmup` sends requests with each Account's token outside Claude Code, reusing Claude Code's system prompt.
