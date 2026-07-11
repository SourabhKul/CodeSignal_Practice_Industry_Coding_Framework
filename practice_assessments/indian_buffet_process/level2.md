# Scenario

Implement an in-memory Indian Buffet Process simulator. All Level 1 behavior remains valid.

## Level 1 - Initial Design & Basic Functions

- **add_customer(selection_tickets, new_dish_count)**
- **customer_dishes(customer_number)**
- **dish_popularity(dish_number)**

## Level 2 - Data Structures & Data Processing

- **feature_matrix()**
  - Return the realized binary customer-by-dish matrix.
  - Rows are customer order; columns are dish creation order. Use `1` when a customer selected a dish and `0` otherwise.
- **popular_dishes(min_popularity)**
  - Return `(dish_number, popularity)` tuples for dishes with popularity at least `min_popularity`.
  - Order results by popularity descending, then dish number ascending.
  - Return `[]` when `min_popularity` is not a positive integer.
- **expected_new_dishes()**
  - Return the exact expected number of new dishes for the next customer as a `fractions.Fraction`.
  - With `n` existing customers, this is `alpha / (n + 1)`.

