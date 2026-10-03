---
name: connect
description: Connect Claude (the Claude app, Cowork, or Claude Code) to Mizan Platform, or fix a broken connection. Use when the user wants to set up Mizan, sign in, "connecte-toi à Mizan", switch company, change the access level, or when the Mizan tools are missing, ask for authentication, or answer 401.
---

# Connect to Mizan

Mizan uses a browser sign-in (OAuth). No token is copied by hand: Claude keeps the connection and
renews it on its own.

First work out where the user is. In a terminal with slash commands, they are in **Claude Code**.
Otherwise they are in the **Claude app** (Cowork or chat). Give only the steps for their client, in
plain words, one step at a time.

## First connection (about one minute)

Open the sign-in:

- **Claude app** (desktop, claude.ai, Cowork): **Settings → Connectors → Add**, add a custom
  connector named **Mizan** with the address `https://mizan.141-94-76-77.sslip.io/mcp` (or the
  address the user's firm gave them, ending in `/mcp`), then **Connect**. A connector that comes
  with the plugin shows "Connects in sessions" instead and is signed in from inside a session.
- **Claude Code** in a terminal: run `/mcp`, select **mizan** and choose **Authenticate**. In the
  desktop app, `/mcp` opens the same Connectors settings as above.

Never set up both a custom connector and the plugin's connector in the same place: Mizan would
appear twice.

Mizan opens in the browser. Then:

1. Sign in with the usual Mizan email and password (and TOTP code if enabled).
2. On the Mizan authorization page:
   - pick the **company** (dossier), or **Tous mes dossiers**;
   - pick the **access level**:
     - **Lecture**: reads only. Best for questions and reports.
     - **Proposition** (recommended): the agent prepares entries that a human approves in
       *Approbations*.
     - **Écriture**: the agent writes, always after a dry-run it must confirm.
   - confirm with the password (or TOTP code), then **Autoriser**.
3. Back in Claude, mizan shows as connected. Check with the `status` skill.

Recommend the lowest level that does the job. The agent never does more than the user's own role
allows, and can never close a period, validate, or change settings, roles or members.

## Switch company or level

A connection is tied to one company (or Tous mes dossiers) and one level. To change it, disconnect
mizan and connect again, then pick the other company or level:

- **Claude app**: **Settings → Connectors** → **Mizan** → disconnect, then connect again.
- **Claude Code**: `/mcp` → **mizan** → **Clear authentication**, then **Authenticate**.

## Remove access

In Mizan, **Découverte → Assistant IA (MCP)**: the connection is listed as "connexion OAuth" and can
be revoked. A company administrator can revoke it too. It also ends on its own after 90 days.

## Troubleshooting

| Symptom | Fix |
|---|---|
| mizan asks to connect or authenticate | Run the sign-in above again |
| The browser says "Connexion impossible" | Start the sign-in again from Claude; the link was incomplete or stale |
| "Mot de passe ou code incorrect" | Re-enter the password; after 5 failures the account locks for a while |
| No company in the list | The account is not a member of any company yet: ask the accounting firm |
| `403` on a write | The level is Lecture, or the user's role does not allow it: reconnect with another level or ask the firm |
| mizan missing entirely | Claude app: add the custom connector (above). Claude Code: `/plugin` → enable mizan |

Never ask the user for their password or a token in the chat. Sign-in happens only in the browser.
