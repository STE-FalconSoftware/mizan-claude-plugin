# Mizan Platform for Claude Code

Run your Mizan Platform company from Claude Code: invoices, purchases, bank reconciliation,
TVA and RAS declarations, payroll, month-end close and reports. Every write goes through Mizan's
dry-run and confirmation step.

## Use in the Claude app (desktop, claude.ai, Cowork)

The simplest path needs no plugin: **Settings → Connectors → Add** a custom connector named Mizan
with the address `https://mizan.141-94-76-77.sslip.io/mcp`, then **Connect** and sign in to Mizan in
the browser. The step-by-step guide for clients is at `/guide/ia` on the Mizan site.

To get the task skills too, install the plugin from this repository, which keeps it up to date:
**Customize → Plugins → Add marketplace**, enter `STE-FalconSoftware/mizan-claude-plugin`, turn on
**Sync automatically**, then install **mizan** and connect it from its **Connectors** tab. Keep only
one Mizan connector (remove the custom one above if you added it). Offline alternative: upload
`dist/mizan.plugin` built with `python scripts/build_cowork.py`.

## Install in Claude Code

```
/plugin marketplace add https://github.com/STE-FalconSoftware/mizan-claude-plugin.git
/plugin install mizan@mizan
```

Then run `/mcp`, select **mizan** and choose **Authenticate**. Mizan opens in your browser: sign in,
pick the company and the access level, and confirm with your password. That's it: no token to
copy, and Claude Code renews the connection on its own.

Run `/mizan:status` to check which company and access level the agent sees.

**"Unknown skill" after an install or update?** The session started before the plugin was
installed or updated. Run `/reload-plugins` (or restart Claude Code); the Mizan tools may work
while the skills are still missing, because they load separately.

The plugin connects to `https://mizan.141-94-76-77.sslip.io/mcp`. A firm hosting Mizan elsewhere builds
its own copy with `python scripts/build_cowork.py --url https://its-address`.

## Skills

| Skill | What it does |
|---|---|
| `/mizan:connect` | Step-by-step sign-in, switching company or level, and troubleshooting |
| `/mizan:status` | Which company, access level, instructions and pending work the agent sees |
| `/mizan:switch` | Switch company inside the session ("passe sur Atlas") or change the access level |
| `/mizan:dossier-setup` | Get a new company ready to keep books: treasury accounts, opening balances, tiers |
| `/mizan:sales` | Quotes, invoices, credit notes, receivables, customer payments |
| `/mizan:purchases` | Supplier invoices (including scanned pièces), purchase orders, recurring bills |
| `/mizan:bank-reconciliation` | Import a bank statement and match it |
| `/mizan:month-end-close` | The closing checklist, up to closing the period |
| `/mizan:tax-declarations` | TVA, RAS certificates, DGI declaration, TEJ, FEC and TEIF exports |
| `/mizan:payroll` | Payroll preview and run, leave, attendance |
| `/mizan:reports` | Financial statements, balances, aging, and an owner's summary |
| `/mizan:cabinet-onboarding` | For accounting firms: add a client company and give its owner a login |

`mizan-basics` loads automatically: it holds the ground rules (firm instructions first, NCT account
codes, TND with 3 decimals, confirm before writing).

## Access levels

A connection is for one company, or for **Tous mes dossiers** (every company you can open in Mizan;
you switch by asking Claude). It lasts at most 90 days. The agent can never do more than
your own role allows.

- **Lecture**: reads only.
- **Proposition**: the agent prepares entries that a person approves in *Approbations*.
- **Écriture**: the agent writes, after showing you a dry-run and getting your confirmation.

Moving real money, deletions, the year-end close, and access or settings changes are never done by
an agent. Every connection is listed in Mizan under **Découverte → Assistant IA (MCP)**, where you
can revoke it.
