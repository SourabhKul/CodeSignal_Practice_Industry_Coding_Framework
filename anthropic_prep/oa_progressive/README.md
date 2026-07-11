# OA Progressive Drills

These drills model the CodeSignal Industry Coding Assessment shape:

- one project-based task
- four progressive levels in 90 minutes
- earlier contracts remain valid
- later levels force extension and refactoring
- standard-library data structures rather than niche algorithms

## Evidence-Based Order

Current reported families:

1. `in_memory_db`
2. `banking_system`
3. `cloud_storage`
4. `recipe_manager`
5. `employee_system`
6. `task_manager`
7. `course_registration`

Transfer drills after those:

- `chinese_restaurant_process`
- `time_versioned_kv`
- `inventory_orders`
- `package_manager`
- `build_system`
- `text_editor`

## Progressive Workflow

Each `solution.py` contains only the Level 1 interface. Read the next level file and add its methods only after the current test passes.

Example:

```bash
cd anthropic_prep/oa_progressive/banking_system
python3 -m unittest test_solution.TestBankingSystem.test_level_1_accounts
```

Reference solutions are for post-run review. To verify the maintained answer keys across all reported scenarios:

```bash
python3 anthropic_prep/oa_progressive/run_reference_tests.py
```
