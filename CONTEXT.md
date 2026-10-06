# claude-swap (personal fork)

Lets one person use several Anthropic Accounts with Claude Code: side by side, or by swapping the Account behind ongoing work.

## Language

**Account**:
An Anthropic login (email plus subscription plan) that owns a usage quota and rate limits.
_Avoid_: login, user, subscription

**Credential**:
The OAuth tokens that authenticate Claude Code as one Account.
_Avoid_: token, auth, key

**Profile**:
A Claude Code configuration home: Sessions, settings, plugins, and MCP server logins. MCP server logins belong to the Profile, never to an Account.
_Avoid_: config dir, account (as a synonym)

**Default Profile**:
The Profile Claude Code uses when no other Profile is selected.
_Avoid_: main profile, global profile

**Instance**:
A running Claude Code process attached to one Profile.
_Avoid_: session (for the process), window

**Parallel Instance**:
An Instance running a non-default Account on that Account's own Profile, alongside other Instances.
_Avoid_: session, session mode

**Session**:
A resumable Claude Code conversation. It lives in a Profile, independent of which Account served it.
_Avoid_: conversation, chat, instance

### Swapping

**Swap**:
Putting another Account's Credential in place of the one currently in use.
_Avoid_: toggle, relogin

**Cold Swap**:
A Swap that takes effect by restarting the Instance and resuming its Session.

**Hot Swap**:
A Swap the running Instance picks up without restarting.
_Avoid_: live switch

**Rollback**:
Undoing the most recent Swap, restoring the previous Account.
_Avoid_: undo, revert
