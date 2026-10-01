---
name: tax-declarations
description: Tunisian tax work in Mizan — the TVA declaration, retenues à la source and their certificates, DGI declarations, the TEJ export, and FEC and TEIF exports. Use when the user asks about TVA, RAS, the monthly declaration, TEJ or El Fatoora exports.
---

# Tax declarations (fiscalité)

Answer legal questions from Mizan's knowledge base: `kb_search`, then `kb_read`, and cite the
entry id and its source. Say so when an entry is marked 🟡 (to verify). Current rates always come
from `fiscal_parameters` (what the software applies), never from memory.

## Monthly TVA
1. Make sure the month is complete: run the `month-end-close` checklist up to step 6.
2. `tax_declaration` for the period: TVA collectée (4367) minus TVA déductible (4366), the credit
   carried forward, and the droit de timbre.
3. Lay it out the way the user will copy it into the DGI form, and flag any line that does not
   agree with the ledger.
4. `dgi_declaration` produces the declaration data or file when it is needed.

## Retenues à la source (RAS)
- `list_withholding_certificates` lists the certificates; `issue_withholding_certificate` issues
  one and `mark_withholding_declared` records that they were declared.
- `tej_export` builds the TEJ file for the period. A human uploads it to the TEJ portal.

## Exports
- `fec_export` for the year (fichier des écritures comptables).
- `teif_export` for an invoice in the El Fatoora (TEIF) format.

## Obligations calendar
`list_tax_obligations` for the year; `tax_obligation_transition` marks one prepared or not
applicable. Filing and paying taxes are 🔴: explain the steps, and never say something was filed.
