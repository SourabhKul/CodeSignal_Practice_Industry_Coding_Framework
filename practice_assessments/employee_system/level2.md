# Scenario

Implement an employee attendance system. All Level 1 behavior remains valid.

## Level 1 - Initial Design & Basic Functions

- **add_employee(employee_id, position, pay_rate)**
- **clock_in(timestamp, employee_id)**
- **clock_out(timestamp, employee_id)**
- **get_total_time(employee_id)**

## Level 2 - Data Structures & Data Processing

- **top_employees(position, n)**
  - Return up to `n` current employees in that position.
  - Sort by completed office time descending, then employee id ascending.
  - Format results as `employee_id(total_time)`.
