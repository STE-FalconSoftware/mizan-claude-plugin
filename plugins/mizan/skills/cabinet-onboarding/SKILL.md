---
name: cabinet-onboarding
description: For the accounting firm (cabinet) — add a new client company to Mizan, give its owner (gérant) a login, and help them connect their own AI agent. Use when an accountant asks how to add a client, invite an owner, or re-send an invitation.
---

# Onboard a client company (cabinet)

Creating companies and inviting people are access operations, which agents never perform. Guide the
accountant through the web app instead.

## 1. Create the dossier
In Mizan, open **Cabinet → Nouveau dossier client**. Enter the raison sociale, the matricule fiscal and the
fiscal year, and put the owner's e-mail in **E-mail du gérant**. Mizan creates the company with the
standard chart of accounts and makes the accountant its *expert*.

## 2. The owner's login
Mizan e-mails the gérant an invitation, valid for 7 days. They open it, choose their own password,
and land in their company. Nobody else ever knows their password.
If sending fails, the dossier is still created and the dialog offers **Réessayer l'invitation**.
If the invitation was sent but has expired, ask Mizan support to re-send it: today only the
platform operator can re-invite an e-mail that already has an account.

## 3. What the owner can do
The *gérant* role covers sales, purchases, stock, treasury and payroll, can read the accounting, and
can invite their own staff (commercial, paie, lecture). Posting entries, closing periods and the
company settings stay with the cabinet.

## 4. Their AI agent
Send the owner these steps:
1. In Claude Code: `/plugin marketplace add STE-FalconSoftware/mizan-claude-plugin`
2. `/plugin install mizan@mizan`
3. In Mizan: **Découverte → Assistant IA (MCP)**, choose an access level, copy the token.
4. `/plugin` → mizan → Configure → paste the token, then run `/mizan:status`.

## 5. Firm instructions
Standing rules for a dossier (which accounts to use, who validates what) go into
**Mémoire → Instructions**. Every agent reads them first through `memory_context`.
