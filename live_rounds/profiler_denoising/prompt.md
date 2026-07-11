# Live Drill: Profiler Denoising

Sampling profilers often produce stack snapshots over time.

Implement `stacks_to_events(samples, min_duration=0)`.

Input:

```python
[
    (0, ["main"]),
    (1, ["main", "a"]),
    (3, ["main", "a", "b"]),
    (5, ["main", "a"]),
    (6, ["main"]),
    (7, []),
]
```

Output events use half-open intervals:

```python
[
    {"name": "main", "start": 0, "end": 7},
    {"name": "a", "start": 1, "end": 6},
    {"name": "b", "start": 3, "end": 5},
]
```

Requirements:

- Handle recursion by treating stack frames by depth, not just name.
- Close frames when the stack shrinks or changes.
- Drop events shorter than `min_duration`.

