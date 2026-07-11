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
- **calculate_salary(employee_id, start_timestamp, end_timestamp)**

## Level 4 - Extending Design & Functionality

- **define_double_pay_period(start_timestamp, end_timestamp)**
  - Add a half-open interval during which worked time earns double pay.
  - Return `False` when `start_timestamp >= end_timestamp`; otherwise return `True`.
  - Overlapping double-pay periods still produce only double, not triple, pay.

`calculate_salary` must now account for double-pay intervals.
