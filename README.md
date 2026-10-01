# Mizan Platform for Claude Code

Run your Mizan Platform company from Claude Code: invoices, purchases, bank reconciliation,
TVA and RAS declarations, payroll, month-end close and reports. Every write goes through Mizan's
dry-run and confirmation step.

## Install

```
/plugin marketplace add STE-FalconSoftware/mizan-claude-plugin
/plugin install mizan@mizan
```

Claude Code then asks for two settings:

| Setting | Where to find it |
|---|---|
| **Mizan address** | Keep the default unless your accounting firm gave you another one. |
| **Agent token** | In Mizan: open your company → **Découverte → Assistant IA (MCP)** → choose an access level → copy the token. It is stored in your system keychain. |

Check with `/mcp` (mizan should be *connected*), then run `/mizan:status`.

## Skills

| Skill | What it does |
|---|---|
| `/mizan:connect` | Step-by-step connection and troubleshooting (expired or revoked tokens, wrong company) |
| `/mizan:status` | Which company, access level, instructions and pending work the agent sees |
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

A token belongs to one company and lasts 30 days by default. The agent can never do more than your
own role allows.

- **Lecture**: reads only.
- **Proposition**: the agent prepares entries that a person approves in *Approbations*.
- **Écriture**: the agent writes, after showing you a dry-run and getting your confirmation.

Moving real money, deletions, the year-end close, and access or settings changes are never done by
an agent.
