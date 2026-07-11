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

The simulator now supports named snapshots.

- **save(name)**
  - Save an independent copy of the current seating state.
  - Return `False` if the name already exists; otherwise return `True`.
- **restore(name)**
  - Replace the current seating state with an independent copy of the named snapshot.
  - Return `False` when the snapshot does not exist; otherwise return `True`.
  - Restoring a snapshot does not delete it or any other snapshot.
- **delete_snapshot(name)**
  - Delete a snapshot and return `True`, or return `False` when it does not exist.

A restore also restores the next table number. Seating after a restore must behave as though later customers and tables had never existed.

