---
name: switch
description: Switch the company (dossier) Claude works in, or change the access level of the Mizan connection. Use when the user says "passe sur X", "travaille sur la société Y", "switch to company Z", "je veux que tu puisses écrire", or asks which company is active.
---

# Switch company or access level

## Switch company (no re-login)

If the connection was granted for **Tous mes dossiers** (all my companies):

1. Call `use_company` with what the user said: a name ("Atlas"), a matricule fiscal, or an id.
   If several companies match, show the candidates and ask which one.
2. Call `memory_context`: each company has its own instructions, and they apply from now on.
3. Confirm in one line: "Je travaille maintenant sur **{raison sociale}** ({matricule})."

Every preview and result names the company. Never write without an active company. If the user
did not say which one, ask.

If the connection is for **one company only**, `use_company` refuses other companies. Offer to
reconnect: `/mcp` → **mizan** → **Clear authentication** → **Authenticate**, and choose either the
other company or **Tous mes dossiers** on the Mizan page.

## Change the access level

The level (Lecture, Proposition, Écriture) is chosen on the Mizan sign-in page and cannot be raised
from the chat, so that a prompt can never give an agent more rights. To change it:

1. `/mcp` → **mizan** → **Clear authentication**.
2. **Authenticate** again and pick the new level (and the company, or Tous mes dossiers).
3. `/mizan:status` to check.

Recommend the lowest level that does the job, and go back down afterwards.
