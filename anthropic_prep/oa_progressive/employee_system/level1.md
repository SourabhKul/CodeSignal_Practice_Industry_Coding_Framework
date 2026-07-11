# Scenario

Implement an employee attendance system. Timestamps are integers and arrive in increasing order.

## Level 1 - Initial Design & Basic Functions

- **add_employee(employee_id, position, pay_rate)**
  - Add an employee and return `True`; return `False` for a duplicate id.
- **clock_in(timestamp, employee_id)**
  - Start a work session and return `True`.
  - Return `False` for a missing employee or one already clocked in.
- **clock_out(timestamp, employee_id)**
  - Finish a work session and return `True`.
  - Return `False` for a missing employee or one not clocked in.
- **get_total_time(employee_id)**
  - Return total time across completed sessions, or `None` for a missing employee.
