# Statement read-back

The coordinator prepares a minimal packet. Include the declaration, definitions of project-specific terms and the imports needed to interpret notation. Strip comments that quote the informal goal, proof bodies, source links, task names that reveal the answer, and earlier reviews. Use neutral names where they carry the expected interpretation. Keep a mapping to the exact reviewed source.

## Prompt for the reader

Read only the supplied Lean declarations and definitions. Translate them into the requested natural language. State each quantifier in order, its domain, hypotheses, conclusion, and the direction of each implication. Explain notation that affects scope or boundary cases. Identify terms whose meaning you cannot determine from the packet. Return the translation before seeing the author's wording.

## Coordinator comparison

Compare the two texts clause by clause. In particular check implicit positivity, natural subtraction, strict inequalities, converse directions and vacuity. Record the original response, any mismatch, the corrected declaration, and the outcome. If prior context or workspace access exposed the expected claim, describe the actual independence. The audit concerns the statement's meaning; the Lean build checks its proof.
