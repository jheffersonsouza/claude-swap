# Rate limits and multi-Account policy

Status: ready-for-agent

## Question

What limits apply when one person runs several Accounts at once from one machine, and what do Anthropic's terms say about it?

- Are subscription limits (Pro, Max, Team) enforced per Account, per organization, per IP, or per device?
- Are there reports of throttling, captchas or bans when 3 to 5 Accounts run at once from one IP?
- What do the consumer terms, commercial terms and usage policy say about:
  - one person holding several Accounts and moving Credentials between them;
  - a third-party tool refreshing tokens and polling usage with Claude Code's OAuth client, as claude-swap does in `src/claude_swap/oauth.py`?

Write the findings, with sources, to `.scratch/fork-adaptation/research/rate-limits-and-policy.md`.
