# Continuing a proof

Keep one current handoff in the user's proof project. A short proof needs only a few lines. For a multi-session proof, maintain a table like this with real declarations and evidence paths.

| Node | Exact proposition or declaration | Depends on | Status and evidence |
| --- | --- | --- | --- |
| Root | Named, frozen proposition | Named lemmas | Open until the assembled root passes its audit |
| Reduction | Implication from the remaining subclaims | Explicit hypotheses | Build command or failed goal |
| Leaf | Smallest pending claim on this route | Earlier facts | Known cases, obstruction, next test |

Preserve the original statement and reviewed version, source revision, toolchain and manifest revision, read-back outcome, last verified theorem, and audit output. Give the strongest unconditional conclusion and the precise open obligation. For a computational experiment record its domain. For a paper result record whether the proof has been formalized.

At handoff, record the mode used in this run, the last chosen route and its reason, and any pending direction question with its options. Preserve the user's explicit route constraints on resume. Revisit a pending choice only if it still matters under the newly selected mode and the current evidence.

When resuming, compare the recorded identities with the working sources. Recheck affected nodes after changes. Choose one open obligation with a mathematical test that can advance or eliminate the route. When the root has been assembled, rerun the audit on the root itself.
