# Scenario

Implement an in-memory task-management system. All previous behavior remains valid.

## Level 1 - Initial Design & Basic Functions

- **add_task(task_id, priority)**
- **update_task(task_id, new_priority)**
- **get_task(task_id)**

## Level 2 - Data Structures & Data Processing

- **search_tasks(min_priority, max_priority)**

## Level 3 - Refactoring & Encapsulation

- **add_user(user_id, quota)**
- **assign_task_at(timestamp, task_id, user_id, ttl)**
- **active_tasks_at(timestamp, user_id)**

## Level 4 - Extending Design & Functionality

- **complete_task_at(timestamp, task_id)**
  - Expire assignments first.
  - Complete a currently active assigned task and return `True`; otherwise return `False`.
  - Completion frees the user's quota.
- **overdue_tasks(timestamp)**
  - Expire assignments first and return task ids that expired without completion, sorted lexicographically.
