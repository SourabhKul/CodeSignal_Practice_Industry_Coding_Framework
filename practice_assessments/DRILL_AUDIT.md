# Drill Design Notes

## Framework Alignment

- One project-based scenario per folder.
- Four cumulative levels intended for a 90-minute run.
- Level 1 uses three or four basic methods and simple data structures.
- Level 2 adds filtering, sorting, ranking, aggregation, or export behavior.
- Level 3 adds entities, timestamps, TTL, permissions, or history and forces refactoring.
- Level 4 extends the existing design without breaking earlier contracts.
- All drills use only the Python standard library.

## Practice Mechanics

- `solution.py` is the candidate workspace and begins with only Level 1 APIs.
- `reference_solution.py` is for post-run review.
- `test_solution.py` imports the candidate module normally and the reference module when `SOLUTION_MODULE=reference_solution` is set.
- `verify_structure.py` detects missing files, future-API leaks, and missing level tests.
- `run_reference_tests.py` verifies maintained answer keys.

## Limitation

Local files cannot hide tests or prevent a reader from opening future levels. The progressive workflow relies on practice discipline; a hosted assessment can gate levels and use hidden tests.
