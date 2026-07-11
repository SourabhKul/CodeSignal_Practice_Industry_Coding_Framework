# Anthropic CodeSignal Practice Pack

This pack separates the 90-minute progressive online assessment from later CodeSignal-hosted live interviews.

## OA Practice

Highest-signal reported scenario families:

1. `oa_progressive/in_memory_db`
2. `oa_progressive/banking_system`
3. `oa_progressive/cloud_storage`
4. `oa_progressive/recipe_manager`
5. `oa_progressive/employee_system`
6. `oa_progressive/task_manager`
7. `oa_progressive/course_registration`

The remaining OA folders are transfer drills. They exercise similar state, sorting, history, or refactoring skills but are not labeled as confirmed Anthropic questions.

For a timed run:

1. Start a 90-minute timer.
2. Open only `level1.md` and `solution.py`.
3. Run only the Level 1 test named in `prompt.md`.
4. Open the next level only after the current level passes.
5. Do not open `reference_solution.py` until the timed attempt and review are finished.

Candidate files expose only Level 1 APIs. Add later APIs yourself as each level unlocks.

## Live-Round Practice

The `live_rounds/` folder covers web crawling, profiler reconstruction, tokenizer review, duplicate files, and cache persistence. These are separate from the progressive ICA. Use a 55-minute timer and explain concurrency, I/O, failure modes, and scaling tradeoffs aloud.

## Commands

```bash
python3 anthropic_prep/oa_progressive/verify_structure.py
python3 anthropic_prep/oa_progressive/run_reference_tests.py
python3 -m compileall -q anthropic_prep
```
