# Scenario

Implement an in-memory Chinese Restaurant Process simulator.

Construct `ChineseRestaurant(alpha)` with a positive integer concentration parameter. Customer `1` is seated automatically at table `1`.

When `n` customers are seated, the next arrival supplies an integer ticket in `[0, alpha + n - 1]`:

- a ticket less than `alpha` opens the next table;
- otherwise, ticket `alpha + i` chooses the table occupied by customer `i + 1`.

Choosing an existing customer this way selects each table with probability proportional to its current size.

## Level 1 - Initial Design & Basic Functions

- **seat(ticket)**
  - Seat one new customer and return their table number.
  - Return `None` without changing state if `ticket` is outside the valid range for the current customer count.
- **customer_table(customer_number)**
  - Return the customer's table, or `None` when the positive one-based customer number does not exist.
- **table_size(table_number)**
  - Return the table's current size, or `0` when the positive one-based table number does not exist.

Tables are numbered consecutively in creation order. Aim for `O(1)` time per operation.

