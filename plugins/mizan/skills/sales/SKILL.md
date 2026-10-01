---
name: sales
description: Sales in Mizan — customers, devis (quotes), factures, avoirs (credit notes), receivables and payment reminders. Use when the user wants to invoice, quote, issue a credit note, record a customer payment or chase a customer.
---

# Sales (ventes)

The confirm-before-write rules in `mizan-basics` apply to every step.

## Invoice a customer
1. `find_customer`. Use `create_customer` only once the user confirms the customer is new.
2. `find_article` for each line. If an article is missing, ask before `create_article`.
3. `create_invoice`, then show the dry-run: lines, HT, TVA per rate, droit de timbre, TTC, due date.
4. When the user says yes, call it again with `confirm: true` and give the invoice number.
5. Run `accounting_controls`.

To quote first: `create_quote`, then `quote_transition` (send / accept / reject) and, once
accepted, `convert_quote_to_invoice`. A draft invoice (from a quote, a recurring template or a
scanned pièce) is issued with `issue_invoice`. Delivery notes: `create_delivery_note`,
`delivery_note_transition`, `list_delivery_notes`.

## Credit note (avoir)
An issued invoice cannot be cancelled. It is corrected with an avoir:
`list_invoices` → `create_credit_note` on that invoice → confirm → `accounting_controls`.

## Who owes us?
- `receivables_aging` for the buckets (0–30, 31–60, 61–90, over 90 days).
- `tiers_balance` (kind customer) for balances, and `general_ledger` filtered on `customer_id` for
  one customer's statement.
- For each overdue customer, `record_reminder` files the relance and produces the letter (it does
  not e-mail anyone); `list_reminders` shows the history. Draft the message in the user's
  language; a human sends it.

## Payment received
`list_treasury_accounts` → `record_payment` (dry-run, then confirm) → `lettrage_suggestions` →
`apply_lettrage`.
