---
name: ai4math
description: Formalize, prove, disprove, or resume a mathematical claim in a local Lean 4 project. Use for statement read-back, lemma decomposition, Mathlib search, and reproducible proof and axiom checks.
---

# AI4Math

Work in the user's proof project. Keep the skill installation separate from the project's sources and research notes. Reuse an existing Lake project and its lockfile. For a new project or the small working example see [setup](references/setup.md).

## Fix the claim

Record the user's exact mathematical claim, domain, quantifier order, conventions, and requested direction. Give the main target a stable name, e.g. `def Target : Prop := ...`, in a statement module containing definitions only. This packages an open problem without asserting an inhabitant. Check definitions, boundary inputs, empty or vacuous cases, and both directions of an equivalence where relevant. Keep the original wording and the reviewed Lean declaration together for comparison. Record a source revision or digest for the statement module and its local definitions.

Use [the read-back guide](references/readback.md) to check the translation. Give an independent reader the declarations and guide only when an isolated reviewer is available and authorized. Compare the response to the original, resolve discrepancies and repeat after meaning-changing edits. If the same assistant is the only reader, record a self-check. Ask the author when a genuine ambiguity changes the theorem. Continue independent work while it is unresolved.

## Develop the proof

1. Search the project's pinned library first. Use local source search for definitions and lemmas, `#check` for exact signatures, and `exact?` or `apply?` on the current goal. Record the names, types and hypotheses of results actually used.
2. Try a direct argument or a counterexample. For a longer proof write the proposed implication from explicit subclaims to the target. Formalize this implication with ordinary arguments for the missing subclaims. Give each open node a precise statement, dependencies, and at least one route to test it.
3. Work on a leaf whose proof or failure changes what can be concluded. Compile small modules as you go. Track circular routes, failed strategies, and the reason each failed. A disproved intermediate claim closes that route; a verified witness contradicting the original claim establishes a disproof.
4. Reassemble the root with actual proofs. For a disproof freeze the proposition `¬ Target` as the counterclaim and audit its proof. Keep explorations containing placeholders in draft files outside the verified import closure.

## Verify and report

Rebuild the exact root module from the recorded source revision. For reproducible delivery, use a fresh project build directory or a clean checkout with the same pinned dependencies. Inspect verified project sources for placeholders, added axioms and native-computation shortcuts. Check definitions and local imports for changes since read-back. Use the named final theorem in the audit, including its transitive axiom dependencies.

From the installed skill folder run (Python 3 and Lake on PATH):

```sh
python scripts/audit.py /path/to/project Proof.Main Proof.result Proof.Target
```

The last name must denote the reviewed closed proposition. The helper builds the module, checks that the proof's inferred type is definitionally equal to this proposition, and reads `#print axioms` from Lean. Its default permits `propext`, `Classical.choice`, and `Quot.sound`; `sorryAx`, native computation axioms, and user axioms fail. Inspect the actual subset and apply any stricter project policy. For names using Lean's quoted identifiers or other valid names outside the helper's ASCII subset, use `lake build +Module` and a separate audit module with the following commands, substituting the actual names. Read the emitted axiom list under the same policy.

```lean
import Proof.Main
private def proofType {α : Sort _} (_ : α) := α
example : proofType (@Proof.result) = Proof.Target := rfl
#print axioms Proof.result
```

Record versions, dependency revisions, source identity, the build and audit commands, exit status, actual axioms and read-back status. Name the strongest established statement. Distinguish bounded evidence, a conditional reduction, a proved lemma, an open root, and a verified proof or disproof of the original claim. To resume across sessions, use [the handoff guide](references/handoff.md) to update the handoff in the proof project with the exact remaining statement and the next mathematical test. On resume check the source identity and pins before reusing evidence.
