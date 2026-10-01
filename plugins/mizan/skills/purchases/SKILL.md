---
name: purchases
description: Purchasing in Mizan — suppliers, purchase orders, supplier invoices (including from a scanned pièce), recurring bills, foreign-currency invoices and payables. Use when the user wants to enter a bill or see what the company owes.
---

# Purchases (achats)

## Enter a supplier invoice
1. `find_supplier`. Create one only after the user confirms it is new.
2. Foreign currency: call `bct_exchange_rate(date, currency)` and pass `currency` and `exchange_rate`.
3. `create_supplier_invoice`, show the dry-run (HT, TVA déductible, FODEC, timbre, RAS if any),
   then confirm.
4. Run `accounting_controls`.

## From a scanned pièce
If the user gives you a file (PDF or image), send it with `upload_document` (small files work best
over the network). Mizan also reads the pièces uploaded in the app. `list_ingestions` → `get_ingestion` → check the
supplier, date, amounts and TVA it extracted with the user → `accept_ingestion`.

## Recurring bills
`recurring_supplier_due` → show what is due → `run_recurring_supplier` (confirm).

## Purchase orders and receipts
`list_purchase_orders`, `create_purchase_order` (dry-run, then confirm), and when goods arrive
`receive_purchase_order` (`list_goods_receipts` for history). A draft supplier invoice is recorded
with `record_supplier_invoice`; a supplier credit note with `create_supplier_credit_note`.

## What do we owe?
`payables_aging`, `tiers_balance` (kind supplier), `list_supplier_invoices`.
Paying a supplier moves real money. The agent may **record** a payment that was already made
(`record_payment`) but never start one.
