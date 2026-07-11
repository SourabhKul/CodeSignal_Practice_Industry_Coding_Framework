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

- **add_tag(customer_number, tag)**
- **customers_with_tag(tag)**
- **recommend_dishes(customer_number, limit)**

## Level 4 - Extending Design & Functionality

- **save(name)**
  - Save an independent copy of the realized feature matrix and customer tags.
  - Return `False` when the name already exists; otherwise return `True`.
- **restore(name)**
  - Replace the current buffet state with an independent copy of a saved state.
  - Return `False` when the snapshot does not exist; otherwise return `True`.
  - Restoring also removes customers, dishes, and tags created after the snapshot. Snapshots themselves remain available.

