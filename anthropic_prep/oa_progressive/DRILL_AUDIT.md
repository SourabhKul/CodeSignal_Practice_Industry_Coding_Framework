# Drill Audit Against CodeSignal ICA Guidance

## Current Design

- One project-based scenario per folder.
- Four cumulative levels intended for a 90-minute run.
- Level 1 candidate files do not reveal later method signatures.
- Level 2 emphasizes filtering, sorting, ranking, or aggregation.
- Level 3 adds entities, timestamps, TTL, permissions, or history and forces refactoring.
- Level 4 extends the existing design while preserving earlier contracts.
- OA drills use the Python standard library only.

## Evidence Corrections

- Added `recipe_manager`, `employee_system`, and `course_registration` from concrete public reports.
- Replaced the old dependency-graph `task_manager` with the reported priority, quota, TTL, completion, and overdue-history family.
- Kept `in_memory_db`, `banking_system`, and `cloud_storage` as the highest-priority repeated-report families.
- Relabeled package, build, inventory, time-versioned KV, and text-editor scenarios as transfer drills rather than claimed Anthropic coverage.

## Practice Mechanics

- `solution.py` is the candidate workspace and initially contains only Level 1 APIs.
- `reference_solution.py` is for post-run review in reported-family folders.
- `test_solution.py` uses the candidate module normally and the reference module when `SOLUTION_MODULE=reference_solution` is set.
- `verify_structure.py` now detects missing files, future-API leaks, and missing level tests.
- `run_reference_tests.py` verifies every maintained answer key.

## Known Limitation

Local files cannot truly hide tests or prevent someone from opening future levels. The workflow relies on practice discipline. CodeSignal's actual platform provides gated levels and hidden scoring tests.
