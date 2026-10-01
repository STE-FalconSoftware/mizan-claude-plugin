---
name: bank-reconciliation
description: Bank reconciliation (rapprochement bancaire) in Mizan — import a bank statement, match its lines to payments and invoices, and explain what is left. Use when the user shares a relevé bancaire or asks to reconcile the bank.
---

# Bank reconciliation

1. `list_treasury_accounts` to pick the bank account. Ask if there are several.
2. If the user gives a statement file (CSV, OFX or an Excel export), stage it with
   `stage_bank_statement`. Otherwise use an existing import:
   `list_bank_statement_imports` → `get_bank_statement_import`.
3. Call `bank_match_suggestions` and show them as a table:
   date · label · amount · proposed match · confidence.
4. Apply only the matches the user approves, with `apply_bank_match` (dry-run, then confirm).
5. For each unmatched line, suggest what it probably is (bank fees on 627, agios on 6511, a customer
   receipt not yet recorded, and so on) and offer to record it with `record_payment` or
   `post_journal_entry`. Each one is confirmed separately.
6. Finish with `accounting_controls`, and give the remaining gap between the statement and the
   bank account balance (`general_ledger` on that account).
