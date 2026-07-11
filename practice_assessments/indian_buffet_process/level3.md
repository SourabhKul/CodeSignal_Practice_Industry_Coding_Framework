# Scenario

Implement an in-memory Indian Buffet Process simulator. All previous behavior remains valid.

## Level 1 - Initial Design & Basic Functions

- **add_customer(selection_tickets, new_dish_count)**
- **customer_dishes(customer_number)**
- **dish_popularity(dish_number)**

## Level 2 - Data Structures & Data Processing

- **feature_matrix()**
- **popular_dishes(min_popularity)**
- **expected_new_dishes()**

## Level 3 - Refactoring & Encapsulation

The simulator now supports labels and feature recommendations for observed customers.

- **add_tag(customer_number, tag)**
  - Add a string tag to a customer.
  - Return `True` only when the customer exists and the tag was not already present; otherwise return `False`.
- **customers_with_tag(tag)**
  - Return matching customer numbers in ascending order.
- **recommend_dishes(customer_number, limit)**
  - Return up to `limit` dishes the customer has not selected.
  - Order candidates by current popularity descending, then dish number ascending.
  - Return `None` for an invalid customer and `[]` when `limit` is not a positive integer.

