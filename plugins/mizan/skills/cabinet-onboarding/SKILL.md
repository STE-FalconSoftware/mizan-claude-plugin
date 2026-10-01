---
name: cabinet-onboarding
description: For the accounting firm (cabinet) — add a new client company to Mizan, give its owner and staff access with the right rights, and help them connect their own AI agent. Use when an accountant asks how to add a client, invite someone, choose what a client can see, or re-send an invitation.
---

# Onboard a client company (cabinet)

Creating companies and giving access are human operations: agents never perform them. Guide the
accountant through the web app.

## 1. Create the dossier
In Mizan, **Cabinet → Dossiers → Nouveau dossier**. Enter the raison sociale, the matricule fiscal
and the fiscal year, and the owner's e-mail. Mizan creates the company with the standard chart of
accounts and makes the accountant its *expert*.

## 2. Give access (« Donner accès »)
From the new dossier's confirmation, from **Cabinet → Clients & accès**, or from **Membres** inside
the company. Pick what the person can do:

| Choice | For whom |
|---|---|
| Tout gérer | The gérant: sales, purchases, stock, treasury and payroll; reads the accounting; invites colleagues |
| Commercial | Sales, purchases and stock only |
| Paie & RH | Employees, leave and payroll only |
| Lecture seule | Reads everything, changes nothing |
| Personnaliser | Module by module: none, read or write (accounting is read-only for clients) |

The person receives an e-mail, chooses their own password and lands in their company. Nobody else
ever knows it. The e-mail also links to the guide for connecting Claude Code.

## 3. Follow up
**Cabinet → Clients & accès** lists every client user of the firm with their access and status.
From there: re-send an expired invitation (at most one every 5 minutes), change the access, or
remove someone.

## 4. Their AI agent
Send the owner the guide: `{Mizan address}/guide/claude-code`. In short:
1. `/plugin marketplace add https://github.com/STE-FalconSoftware/mizan-claude-plugin.git`
2. `/plugin install mizan@mizan`
3. `/mcp` → mizan → **Authenticate**, sign in, pick the company and the level.

## 5. Firm instructions
Rules for a dossier or for the whole firm go into **Mémoire → Consignes** (for example "Les frais
bancaires BIAT vont en 627100"). Every agent reads them first through `memory_context`.
