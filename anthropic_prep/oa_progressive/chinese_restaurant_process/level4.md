# Scenario

Implement an in-memory Chinese Restaurant Process simulator. All previous behavior remains valid.

## Level 1 - Initial Design & Basic Functions

- **seat(ticket)**
- **customer_table(customer_number)**
- **table_size(table_number)**

## Level 2 - Data Structures & Data Processing

- **seat_many(tickets)**
- **list_tables()**

## Level 3 - Refactoring & Encapsulation

- **save(name)**
- **restore(name)**
- **delete_snapshot(name)**

## Level 4 - Extending Design & Functionality

- **fork(name)**
  - Return a new, independent `ChineseRestaurant` beginning at the named snapshot.
  - Return `None` when the snapshot does not exist.
  - The fork has the same `alpha` but starts with no named snapshots of its own.
- **compare_snapshots(first, second)**
  - Compare table sizes in two snapshots.
  - Return `None` if either snapshot does not exist.
  - Otherwise return `(table_number, delta)` tuples for tables whose sizes differ, ordered by table number ascending. `delta` is the second snapshot's size minus the first snapshot's size; a missing table has size zero.

Forks and the original restaurant must not share mutable seating state.

