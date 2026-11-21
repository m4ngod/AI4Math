# Local setup

Start in the chosen proof directory. Inspect `lean-toolchain`, `lakefile.toml` or `lakefile.lean`, and `lake-manifest.json`. Use the project's Lean and Lake. Record the actual output of `lake env lean --version` and `lake --version`. For Mathlib record its resolved Git revision from the manifest. A local path dependency needs its own commit or source digest.

For a new project install Lean tooling using the [Lean setup instructions](https://lean-lang.org/install/). With a current Lake and elan, `lake new MyProof math` creates a project with Mathlib. In the newly created folder run `lake update` to resolve the initial dependencies if needed, then `lake exe cache get` to fetch matching precompiled artifacts. Preserve the resulting toolchain and manifest for subsequent runs. In an existing locked project use its manifest directly. A dependency upgrade is a separate change and requires rebuilding the proof.

A project using only Lean's standard library can omit Mathlib. To run the bundled example from the skill directory with its pinned Lean toolchain available:

```sh
python scripts/audit.py examples/demo Demo Demo.result Demo.Target
```

The initial toolchain and dependency downloads need network access. Once the required toolchain, packages, and build inputs are present, compilation and the audit run on the local machine. The example needs no third-party Lean packages. For real projects, inspect local sources under the package directory specified by Lake, commonly `.lake/packages/mathlib/Mathlib`. See the [community project guide](https://leanprover-community.github.io/install/project.html) and [Mathlib declaration index](https://leanprover-community.github.io/mathlib4_docs/).
