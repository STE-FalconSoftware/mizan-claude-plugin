---
name: mizan-basics
description: Ground rules for every Mizan Platform task (Tunisian NCT accounting, TND with 3 decimals, confirm-before-write tiers, firm instructions). Use whenever a Mizan MCP tool is about to be called.
user-invocable: false
---

# Working with Mizan

Mizan is a Tunisian accounting ERP built on the NCT (Système Comptable des Entreprises,
loi 96-112). It is not the French PCG.

## Every session
- Call `memory_context` first for the company. Its **instructions** are written by humans and must
  be followed. Its **memory** is context and may be out of date. If you rely on an unconfirmed
  memory (one an agent wrote), tell the user before asking them to confirm anything.
- When unsure where something lives, call `erp_guide` (optionally with a category) or `how_to`.
- Memory has two scopes: the dossier (`company`) and the firm (`firm`, shared by all its dossiers).
  You may propose entries in either with `memory_write`; they stay *unconfirmed* until a human
  confirms them on the Mémoire page. Instructions are written by humans only.
- Law, tax rules and accounting standards: `kb_search` / `kb_read` and cite the source.
- On a new or unfamiliar dossier, call `dossier_readiness`: it lists what blocks bookkeeping
  (treasury accounts, chart, opening balances, suppliers not TEJ-ready) and the next step for each.
  The `dossier-setup` skill walks through it.
- `use_company` and `list_companies` return `access_level` (read, propose or write): read it
  instead of guessing from which tools work.

## Writing safely
- 🟢 Reads run freely.
- 🟡 Writes first return a **dry-run**. Show the user the preview in plain words (accounts,
  amounts, parties, dates). Call again with `confirm: true` only after they say yes.
- 🔴 Moving real money, deletions, the year-end close, access and settings are never done by the
  agent. Call `how_to` and explain the steps the human takes.
- After any write that touches the ledger, run `accounting_controls` and report what it flags.

- Bank coordinates (RIB, IBAN) are never set or changed by the agent; Mizan refuses it. A human
  enters them in the app.

## Data conventions
- Resolve names to ids first: `find_customer`, `find_supplier`, `find_article`, `find_employee`,
  `find_account`, `list_treasury_accounts`.
- Use NCT account **codes** (411, 401, 532, 707, 4366, 4367), never UUIDs.
- Amounts are decimal **strings**. TND has 3 decimals (`"1200.500"`).
- A foreign-currency document needs the BCT rate for its date: `bct_exchange_rate`.
- Rates (TVA, RAS, payroll, depreciation) are set per company. Read them, never assume them.
- The chart has about 600 accounts: filter `chart_of_accounts` (`class`, `prefix`,
  `postable_only`) or use `find_account`, never dump it whole.
- Fiscal periods are lazy: an empty `list_fiscal_periods` means every month is open. Nothing has to
  be "opened" before posting.
- A wrong customer or supplier record (country, residency, matricule, TVA regime, address) is
  corrected with `update_customer` / `update_supplier`, which keep every other field. A foreign
  supplier gets `country` (ISO-2), `is_resident: false` and its `foreign_tax_id`.
- Supporting documents (PDF, scans, photos) go through `upload_document`: Mizan reads the text
  layer or, for a scan, the image, and proposes the extracted data. Never invent figures you could
  not read.

## Language
Answer in the user's language (French, Arabic or English) and keep the French accounting terms the
user uses (facture, avoir, lettrage, clôture, déclaration).
