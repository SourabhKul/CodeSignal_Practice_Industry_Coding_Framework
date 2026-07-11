import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main():
    scenarios = sorted(path for path in ROOT.iterdir() if path.is_dir() and (path / "reference_solution.py").exists())
    failed = []
    for scenario in scenarios:
        env = os.environ.copy()
        env["SOLUTION_MODULE"] = "reference_solution"
        result = subprocess.run(
            [sys.executable, "test_solution.py"],
            cwd=scenario,
            env=env,
            text=True,
            capture_output=True,
        )
        if result.returncode == 0:
            print(f"PASS {scenario.name}")
        else:
            failed.append(scenario.name)
            print(f"FAIL {scenario.name}")
            print(result.stdout)
            print(result.stderr)
    if failed:
        raise SystemExit(f"Reference tests failed: {', '.join(failed)}")
    print(f"Reference solutions OK ({len(scenarios)} scenarios)")


if __name__ == "__main__":
    main()
