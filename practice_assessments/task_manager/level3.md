# Scenario

Implement an in-memory task-management system. All previous behavior remains valid.

## Level 1 - Initial Design & Basic Functions

- **add_task(task_id, priority)**
- **update_task(task_id, new_priority)**
- **get_task(task_id)**

## Level 2 - Data Structures & Data Processing

- **search_tasks(min_priority, max_priority)**

## Level 3 - Refactoring & Encapsulation

The system now supports user quotas and expiring assignments. Timestamped methods receive non-decreasing timestamps.

- **add_user(user_id, quota)**
  - Add a user and return `True`; return `False` for a duplicate id.
- **assign_task_at(timestamp, task_id, user_id, ttl)**
  - Assign an existing open, unassigned task for `[timestamp, timestamp + ttl)`.
  - Return `False` for missing entities, an already assigned task, or a user at quota.
- **active_tasks_at(timestamp, user_id)**
  - Expire assignments first, then return the user's active task ids sorted lexicographically.
  - Return `None` for a missing user.
