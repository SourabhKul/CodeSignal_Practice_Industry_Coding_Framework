# Scenario

Implement an in-memory parcel inventory. All previous behavior remains valid.

## Level 1 - Initial Design & Basic Functions

- **add_parcel(parcel_id, size)**
- **get_parcel(parcel_id)**
- **remove_parcel(parcel_id)**

## Level 2 - Data Structures & Data Processing

- **find_parcels(prefix)**
- **top_parcels(count)**

## Level 3 - Refactoring & Encapsulation

The manager now tracks couriers. A parcel's status may change only after a courier has been assigned to that parcel. The status operation does not receive a courier identifier: the only requirement is that some registered courier is currently assigned.

- **add_courier(courier_id)**
  - Register a courier and return `True`; return `False` for an invalid or duplicate identifier.
- **assign_courier(parcel_id, courier_id)**
  - Assign a registered courier to an existing parcel.
  - Return `True` only when the assignment changes; otherwise return `False`.
- **assigned_courier(parcel_id)**
  - Return the assigned courier identifier, or `None` when the parcel is absent or has no courier.
- **update_status(parcel_id, status)**
  - Change an existing assigned parcel's status.
  - Return `True` only when `status` is a non-empty string different from the current status; otherwise return `False`.
