---
name: month-end-close
description: Month-end closing checklist in Mizan — unposted documents, recurring entries, depreciation, controls, TVA, and closing the period. Use when the user asks to close a month, prepare the clôture, or check whether a period is ready.
---

# Month-end close

Run the steps in order and report a checklist with ✅, ⚠️ or ❌ for each.

1. `close_readiness` for the period: the server's own list of blockers.
2. `list_unposted_documents`, then offer `post_document_to_ledger` for them (confirm each batch).
3. `recurring_due` and `recurring_supplier_due`, then `run_recurring` and `run_recurring_supplier`
   if the user agrees.
4. `run_depreciation` for the month (dry-run, then confirm).
5. Bank: check every bank account is reconciled to its statement. If not, offer the
   `bank-reconciliation` skill.
6. `accounting_controls` and `journal_totals`, and `anomalies` for anything unusual.
7. TVA: `tax_declaration` for the month (see the `tax-declarations` skill).
8. `set_period_status` to close the month, only once the user confirms. The year-end clôture is
   done by a human: explain it with `how_to`.
