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
   date · label · amount · proposed match · confidence. Matches are on recorded payments, to the
   millime.
4. Apply only the matches the user approves, with `apply_bank_match` (dry-run, then confirm).
5. A line with no payment may list `invoice_candidates`: open invoices within a few % of the
   amount (the bank kept fees, or the customer withheld RAS). Ask the user which it is, then
   `record_payment` with the invoice's open balance as `amount` and the difference as `bank_fees`
   and/or `ras_withheld` (RAS withheld by a customer goes to 4341), then `apply_bank_match`.
6. For each other unmatched line, suggest what it probably is (bank fees on 6278, agios on 6516, a
   transfer between our own accounts, and so on) and offer to record it with `record_payment`,
   `transfer_funds` or `post_journal_entry`. `classify_bank_line` sets the line's kind (e.g.
   `internal_transfer`) so the reviewer sees it; it books nothing. Each one is confirmed
   separately.
7. Finish with `accounting_controls`, and give the remaining gap between the statement and the
   bank account balance (`general_ledger` on that account).
