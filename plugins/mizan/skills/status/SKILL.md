---
name: status
description: Check the Mizan connection and show which company, access level and pending work the agent sees. Use when the user asks "am I connected", "which company", or at the start of a Mizan session.
---

# Mizan status

1. Call `list_companies`. If it fails, stop and follow the `connect` skill.
2. Call `memory_context` for the company. It returns the firm's and the dossier's instructions,
   which override the general conventions for the rest of the session.
3. Call `close_readiness`, and `list_proposals` if the token allows proposals, to see what is waiting.
4. Answer in one short block:
   - **Company:** name and matricule fiscal
   - **Access:** read, propose or write (deduce it from which tools worked)
   - **Waiting:** unposted documents, pending proposals, period status
   - **Instructions:** one line for each standing instruction from `memory_context`
