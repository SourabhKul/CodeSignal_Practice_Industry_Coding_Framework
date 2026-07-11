# Scenario

Implement an employee attendance and payroll system. All previous behavior remains valid.

## Level 1 - Initial Design & Basic Functions

- **add_employee(employee_id, position, pay_rate)**
- **clock_in(timestamp, employee_id)**
- **clock_out(timestamp, employee_id)**
- **get_total_time(employee_id)**

## Level 2 - Data Structures & Data Processing

- **top_employees(position, n)**

## Level 3 - Refactoring & Encapsulation

- **announce_promotion(employee_id, new_position, new_pay_rate, effective_from)**
  - Store one pending promotion and return `True`.
  - Return `False` for a missing employee or when another promotion is pending.
  - Apply the promotion on the employee's first clock-in at or after `effective_from`.
- **calculate_salary(employee_id, start_timestamp, end_timestamp)**
  - Return pay earned during the half-open interval `[start_timestamp, end_timestamp)`.
  - Count only completed work intervals and use the pay rate active when each interval began.
  - Return `None` for a missing employee.
