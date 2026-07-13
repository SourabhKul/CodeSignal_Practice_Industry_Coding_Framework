# Progressive Practice Assessments

These exercises model the CodeSignal Industry Coding Assessment shape:

- one project-based task with four cumulative levels;
- a 90-minute practice window;
- earlier method contracts remain valid at every level;
- later levels require extension and refactoring with standard-library data structures.

## Drills

Start with the stateful-system scenarios:

1. `in_memory_db`
2. `banking_system`
3. `cloud_storage`
4. `recipe_manager`
5. `employee_system`
6. `task_manager`
7. `course_registration`

Additional transfer drills:

- `chinese_restaurant_process`
- `indian_buffet_process`
- `parcel_manager`
- `time_versioned_kv`
- `inventory_orders`
- `package_manager`
- `build_system`
- `text_editor`

## Workflow

Each `solution.py` exposes only Level 1 APIs. Read the next level file and add methods only after the current level passes.

```bash
cd practice_assessments/banking_system
python3 -m unittest test_solution.TestBankingSystem.test_level_1_accounts
```

Reference solutions are for post-run review. Verify maintained answer keys with:

```bash
python3 practice_assessments/run_reference_tests.py
```

See [`SOURCES.md`](SOURCES.md) for the public framework references and [`DRILL_AUDIT.md`](DRILL_AUDIT.md) for the level-design criteria.
