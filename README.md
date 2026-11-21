# AI4Math

AI4Math helps an agent turn a mathematical claim into Lean 4, develop a proof on your machine, and check exactly what was proved. It runs locally and requires no AI4Math account or API key.

# Paste this into your agent

```text
Follow the setup instructions at https://raw.githubusercontent.com/m4ngod/AI4Math/main/README.md to download and configure AI4Math for my agent, check Python 3, Lean 4 and Lake, install anything missing, and verify the setup by running the bundled proof audit.
```

### Setup instructions for the agent

1. **Install the skill.** Download the complete [AI4Math repository](https://github.com/m4ngod/AI4Math) into the client's supported skills directory as `ai4math`, with `SKILL.md` directly inside it. For a project-scoped Codex installation, use `.agents/skills/ai4math/`. Clone with Git or extract the [repository ZIP](https://github.com/m4ngod/AI4Math/archive/refs/heads/main.zip). Reuse an existing installation and preserve local edits.
2. **Check the tools and install what's missing.** Find a working Python 3 interpreter (`python3`, `python`, or `py -3` on Windows). From `examples/demo/`, run `lean --version` and `lake --version` and check Lean against the bundled `lean-toolchain` file. Install missing tools using the [Python downloads](https://www.python.org/downloads/) and [Lean installation guide](https://lean-lang.org/install/) for the user's OS. Lake ships with Lean. If the pinned toolchain is missing, install that version with elan. Make the tools available to the agent's shell and repeat the checks.
3. **Run the proof audit.** From the installed skill directory, run the command below with the Python 3 interpreter you found. The demo uses Lean's standard library. It proves that a list made by repeating `true` exactly *n* times has length *n*. The audit builds the module, checks that the theorem has the intended type, and reports its axiom dependencies.

```sh
python scripts/audit.py examples/demo Demo Demo.result Demo.Target
```

The last line of a successful run reads `PASS Demo.result has type Demo.Target; axiom dependencies: none`. Report the installation path, tool versions, and audit result. If the client loads skills at session start, tell the user to open a new session to invoke `$ai4math`.

## Using AI4Math

Open a proof project and give `$ai4math` a claim in ordinary language. The agent asks which mode you want in the client's display language. You can also choose a mode in the first message.

- **Semi-auto** suits problems of moderate or lower difficulty when you want to follow the reasoning and choose each major direction. At a fork, the agent links a route comparison before asking you to decide. The document opens with the choices and recommendation, then walks through the proof up to the fork, what each route would establish, and the first test. A worked example can make the key inference easier to see. A brief verification summary links to the detailed calculations and logs. The chooser uses the same route labels, usually with two to five one-sentence options. You can ask for clarification before choosing.
- **Full auto** suits difficult problems such as the Riemann hypothesis or the twin prime conjecture when you want the agent to choose routes even if you cannot follow every step. Where the client supports and enables Goal mode, the agent pursues the original objective across rounds and reuses a matching active goal. Proving a supporting lemma is a checkpoint. If you asked for a specific milestone, that milestone defines completion.

Switch modes at any time. “You choose this time” delegates one decision and keeps semi-auto active. At the end of each full-auto round, the agent records what it tried, what it proved, why a route failed, where the evidence lives, and which gap to test next. Clients without Goal mode can use the same handoff to resume in a later session. A fresh invocation lets you choose the mode again.

## How a proof develops

1. **Fix the claim.** Make the domains, quantifiers, hypotheses and conclusion explicit. When available and authorized, an independent reader translates the Lean statement back into ordinary language so you can compare it with the original.
2. **Find the gap.** Search the project's pinned theorem library, including [Mathlib](https://github.com/leanprover-community/mathlib4) when available. Check the exact hypotheses of relevant results. If they already imply the target, assemble and verify the proof. Otherwise, write down what follows and the precise step still missing. Existing projects keep their Lean and library versions. See the [local setup guide](references/setup.md) for new Mathlib projects.
3. **Invent tools for the missing step.** If an estimate loses the relationship between two objects, try defining a quantity on the pair. State the property that would advance the proof, then test it on an example likely to expose a flaw. Keep unproved ideas as conjectures or explicit hypotheses of a reduction. Record failed approaches so the next round can build on them.
4. **Verify the result.** Prove the properties used by the final argument in Lean, assemble the theorem, and audit its type and transitive axiom dependencies. For a disproof, audit the negation of the claim. If the problem remains open, report the strongest established result, the remaining obligation and a reproducible next test.

[Skill instructions](SKILL.md) · [Statement read-back](references/readback.md) · [Research handoff](references/handoff.md)
