---
name: connect
description: Connect Claude Code to Mizan Platform, or fix a broken connection. Use when the user wants to set up Mizan, log in, change company, renew or replace the agent token, or when the Mizan tools are missing or answer 401.
---

# Connect to Mizan

Mizan lets agents in with an **agent token**. A token belongs to ONE company, has an access level,
lasts 30 days by default (90 at most), and can be revoked at any time from the web app.

## First connection (about one minute)

Take the user through these steps one at a time, waiting for each to be done:

1. Open Mizan in the browser (default `https://mizan.141-94-76-77.sslip.io`) and sign in.
2. Pick the company (dossier), then open **Découverte → Assistant IA (MCP)**.
3. Choose the access level:
   - **Lecture**: reads only. Best for questions and reports.
   - **Proposition**: the agent prepares entries that a human approves in *Approbations*.
   - **Écriture**: the agent can write, always after a dry-run that it must confirm.
   Recommend the lowest level that does the job.
4. Re-enter the password (or the TOTP code) when asked, then copy the token. It is shown only once.
5. In Claude Code run `/plugin`, open **mizan → Configure**, and paste the token into *Agent token*.
   Keep the default address unless the firm gave you another one. The token is stored in the
   system keychain, never in a file.
6. Run `/mcp` and check that **mizan** shows *connected*, then run `/mizan:status`.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `401` with `agent_token_legacy` | Token minted before 2026-09-23 | Mint a new token (steps 2–5) |
| `401`, expired | Older than its lifetime (30 days by default) | Mint a new token |
| `401`, revoked | An admin revoked it in Assistant IA | Ask the dossier admin, then mint a new one |
| Wrong company | A token is tied to one company | Mint a token in the other company and configure it |
| `403` on a write | Read-only token, or the member's role does not allow it | Use a higher level, or ask the cabinet |
| mizan missing from `/mcp` | Plugin disabled or not configured | `/plugin` → enable → Configure |

Never ask the user to paste the token into the chat. It belongs only in the plugin settings.
