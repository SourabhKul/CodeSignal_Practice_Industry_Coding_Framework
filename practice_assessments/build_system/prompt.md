# Build System

This is a medium-priority CodeSignal-style OA drill for dependency ordering, cycle checks, and cache invalidation.

Read `level1.md` through `level4.md` in order and implement only `solution.py`.

Run one level at a time:

```bash
python3 -m unittest test_solution.TestBuildSystem.test_level_1_targets
python3 -m unittest test_solution.TestBuildSystem.test_level_2_order
python3 -m unittest test_solution.TestBuildSystem.test_level_3_recursive_build
python3 -m unittest test_solution.TestBuildSystem.test_level_4_stale_cascade
```

