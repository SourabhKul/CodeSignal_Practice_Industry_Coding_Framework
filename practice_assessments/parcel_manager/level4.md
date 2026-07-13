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

- **add_courier(courier_id)**
- **assign_courier(parcel_id, courier_id)**
- **assigned_courier(parcel_id)**
- **update_status(parcel_id, status)**

## Level 4 - Extending Design & Functionality

The manager records a new version after every successful state-changing operation. Version `0` is the initial empty inventory.

- **rollback(version)**
  - Restore the exact state after the specified version.
  - Return `False` for an invalid version; otherwise return `True`.
  - Discard all later versions after a successful rollback. Later operations create a new branch of history.

Courier registrations, assignments, parcel deletion, and status changes must all be restored correctly.

