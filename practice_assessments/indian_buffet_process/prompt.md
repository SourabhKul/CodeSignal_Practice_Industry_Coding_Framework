# Indian Buffet Process

This is an original progressive practice exercise based on the standard Indian Buffet Process (IBP). It is not a reproduction of proprietary interview content.

Read `level1.md` through `level4.md` one at a time. Implement `solution.py` and run only the current level test:

```bash
python3 -m unittest test_solution.TestIndianBuffet.test_level_1_sampling
python3 -m unittest test_solution.TestIndianBuffet.test_level_2_matrix_and_popularity
python3 -m unittest test_solution.TestIndianBuffet.test_level_3_customer_tags
python3 -m unittest test_solution.TestIndianBuffet.test_level_4_snapshots
```

The simulator uses deterministic tickets for existing dishes and accepts precomputed new-dish counts, avoiding flaky random tests while preserving the IBP selection rule.

