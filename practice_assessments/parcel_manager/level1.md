# Scenario

Implement an in-memory parcel inventory. Every parcel has a unique string identifier, a positive integer size, and an initial status of `"created"`.

## Level 1 - Initial Design & Basic Functions

- **add_parcel(parcel_id, size)**
  - Add a parcel and return `True`.
  - Return `False` when the identifier is not a non-empty string, already exists, or `size` is not a positive integer.
- **get_parcel(parcel_id)**
  - Return a new dictionary with the parcel's `"size"` and `"status"`, or `None` when absent.
- **remove_parcel(parcel_id)**
  - Delete the parcel and return `True`, or return `False` when absent.

Do not expose mutable internal parcel records to callers.
