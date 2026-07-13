# Scenario

Implement an in-memory parcel inventory. All Level 1 behavior remains valid.

## Level 1 - Initial Design & Basic Functions

- **add_parcel(parcel_id, size)**
- **get_parcel(parcel_id)**
- **remove_parcel(parcel_id)**

## Level 2 - Data Structures & Data Processing

- **find_parcels(prefix)**
  - Return identifiers for parcels whose identifiers start with `prefix`, ordered lexicographically.
- **top_parcels(count)**
  - Return up to `count` `(parcel_id, size)` tuples.
  - Order parcels by size descending, then identifier ascending.
  - Return `[]` when `count` is not a positive integer.

