import ast
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REQUIRED = {"level1.md", "level2.md", "level3.md", "level4.md", "prompt.md", "solution.py", "test_solution.py"}
SKIP = {"__pycache__"}


def documented_methods(path):
    return set(re.findall(r"^- \*\*([a-zA-Z_]\w*)\(", path.read_text(), flags=re.MULTILINE))


def solution_methods(path):
    tree = ast.parse(path.read_text())
    return {
        node.name
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and not node.name.startswith("__")
    }


def main():
    problems = []
    scenarios = [path for path in sorted(ROOT.iterdir()) if path.is_dir() and path.name not in SKIP]
    for path in scenarios:
        present = {child.name for child in path.iterdir() if child.is_file()}
        missing = sorted(REQUIRED - present)
        if missing:
            problems.append(f"{path.name}: missing {', '.join(missing)}")
            continue

        level1 = documented_methods(path / "level1.md")
        later = set().union(*(documented_methods(path / f"level{level}.md") for level in range(2, 5))) - level1
        leaked = sorted(solution_methods(path / "solution.py") & later)
        if leaked:
            problems.append(f"{path.name}: solution.py leaks later-level APIs: {', '.join(leaked)}")

        tests = ast.parse((path / "test_solution.py").read_text())
        test_names = [node.name for node in ast.walk(tests) if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")]
        if len(test_names) < 4:
            problems.append(f"{path.name}: expected at least four level tests, found {len(test_names)}")

    if problems:
        print("\n".join(problems))
        raise SystemExit(1)
    print(f"OA progressive structure OK ({len(scenarios)} scenarios, no future-API leaks)")


if __name__ == "__main__":
    main()
