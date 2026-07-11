# CodeSignal Practice: Industry Coding Framework

Original Python practice exercises for CodeSignal-style coding assessments and live coding interviews. They follow the local [Industry Coding Skills Evaluation Framework](<CodeSignal Skills Evaluation Framework.pdf>) without reproducing private assessment content.

## Repository Layout

- [`practice_assessments/`](practice_assessments/README.md) - four-level, 90-minute project drills. Each scenario preserves earlier APIs as requirements grow.
- [`live_rounds/`](live_rounds/README.md) - standalone 45-60 minute coding exercises for a live-interview setting.
- [`CodeSignal Skills Evaluation Framework.pdf`](<CodeSignal Skills Evaluation Framework.pdf>) - the local framework reference used to shape level progression.

## Quick Start

Use Python 3.10 or newer. No third-party packages are required.

```bash
cd practice_assessments/chinese_restaurant_process
python3 -m unittest test_solution.TestChineseRestaurant.test_level_1_seating
```

For a progressive assessment, read only `level1.md` first, implement `solution.py`, and run the matching test named in `prompt.md`. Unlock each next level only after the current one passes. Review `reference_solution.py` only after the timed attempt.

To validate all maintained reference implementations:

```bash
python3 practice_assessments/run_reference_tests.py
```

## Contributing

Add progressive scenarios under `practice_assessments/` with `level1.md` through `level4.md`, `prompt.md`, `solution.py`, `test_solution.py`, and a separate `reference_solution.py`. Keep the exercises deterministic, standard-library-only, and cumulative across levels.
