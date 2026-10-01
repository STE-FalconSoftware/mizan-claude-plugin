---
name: reports
description: Financial reports from Mizan — bilan, compte de résultat, trial balance, general ledger, customer and supplier balances and aging, stock valuation, and an owner's summary. Use when the user asks how the business is doing, for a report, or for figures.
---

# Reports

| Need | Tool |
|---|---|
| Bilan and compte de résultat | `financial_statements` |
| Trial balance (balance générale) | `trial_balance` |
| General ledger, or one party's statement | `general_ledger` (filter on account, `customer_id` or `supplier_id`) |
| Who owes us, whom we owe | `receivables_aging`, `payables_aging`, `tiers_balance`, `tiers_aging` |
| Stock | `stock_level`, `stock_valuation` |
| Health checks | `accounting_controls`, `anomalies` |

## Owner's summary ("how are we doing?")
Build one short brief for the period, next to the same period last year:
- Revenue (70x), gross margin and result, from `financial_statements`
- Cash on the bank and cash accounts (`list_treasury_accounts` balances)
- Receivables over 60 days, and the five largest debtors
- Payables due in the next 30 days
- Anything flagged by `accounting_controls` or `anomalies`

State the period and the date the figures were read. If the period is still open, say the figures
are provisional.
