# Scenario

Implement an in-memory task-management system.

## Level 1 - Initial Design & Basic Functions

- **add_task(task_id, priority)**
  - Add an open task and return `True`; return `False` for a duplicate id.
- **update_task(task_id, new_priority)**
  - Update an open task and return `True`; return `False` when missing or not open.
- **get_task(task_id)**
  - Return `{"priority": priority, "status": status}` or `None` when missing.
