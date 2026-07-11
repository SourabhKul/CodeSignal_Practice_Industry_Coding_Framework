# Scenario

Implement an in-memory task-management system. All Level 1 behavior remains valid.

## Level 1 - Initial Design & Basic Functions

- **add_task(task_id, priority)**
- **update_task(task_id, new_priority)**
- **get_task(task_id)**

## Level 2 - Data Structures & Data Processing

- **search_tasks(min_priority, max_priority)**
  - Return open task ids whose priority is inside the inclusive range.
  - Sort by priority descending, then creation order descending so newer tasks win ties.
  - Return `[]` when nothing matches.
