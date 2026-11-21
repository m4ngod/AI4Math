"""Build a Lake module and check a named proof against a frozen proposition."""
import argparse
import re
import subprocess
import sys
from pathlib import Path


STANDARD_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
NAME = re.compile(r"[A-Za-z_][A-Za-z_0-9']*(?:\.[A-Za-z_][A-Za-z_0-9']*)*")


def run(command, project, source=None):
    proc = subprocess.run(command, cwd=project, input=source, encoding="utf-8",
                          errors="replace", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    sys.stdout.write(proc.stdout)
    if proc.returncode:
        raise SystemExit(proc.returncode)
    return proc.stdout


def audit(project, module, theorem, target):
    run(["lake", "build", "+" + module], project)
    # Give the check its own module. Both operands of Eq are types, so rfl
    # requires definitional equality; implication or coercion cannot bridge them.
    source = f"""import {module}
#check ({target} : Prop)
private def proofType {{α : Sort _}} (_ : α) := α
example : proofType (@{theorem}) = {target} := rfl
#print axioms {theorem}
"""
    output = run(["lake", "env", "lean", "--stdin"], project, source)
    prefix = "'" + re.escape(theorem) + "'"
    empty = re.findall(prefix + r" does not depend on any axioms", output)
    lists = re.findall(prefix + r" depends on axioms:\s*\[([^\]]*)\]", output)
    if len(empty) + len(lists) != 1:
        raise SystemExit("Could not identify one axiom report for the named proof.")
    used = {entry.strip() for entry in lists[0].split(",")} if lists else set()
    unexpected = used - STANDARD_AXIOMS
    if unexpected:
        raise SystemExit("Unapproved axiom dependencies: " + ", ".join(sorted(unexpected)))
    print(f"PASS {theorem} has type {target}; axiom dependencies: "
          + (", ".join(sorted(used)) or "none"))


def main():
    sys.stdout.reconfigure(errors="backslashreplace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    for field in ("module", "theorem", "target"):
        parser.add_argument(field, help="Fully qualified ASCII Lean name")
    args = parser.parse_args()
    for name in (args.module, args.theorem, args.target):
        if not NAME.fullmatch(name):
            parser.error(f"Unsupported Lean name: {name!r}. Use the manual audit in SKILL.md.")
    try:
        audit(args.project, args.module, args.theorem, args.target)
    except OSError as exc:
        parser.exit(1, f"Could not run Lake: {exc}\n")


if __name__ == "__main__":
    main()
