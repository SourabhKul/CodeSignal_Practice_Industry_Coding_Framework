# Scenario

Your task is to implement a simplified version of a key-value store.

## Level 1 - Initial Design & Basic Functions

- **set(key, value)**
- **get(key)**
- **delete(key)**

## Level 2 - Data Structures & Data Processing

- **keys(prefix)**
- **count(prefix)**

## Level 3 - Refactoring & Encapsulation

The store now supports timestamped versions.

- **set_at(timestamp, key, value)**
  - Store `value` for `key` at `timestamp`.
  - Return `None`.
- **delete_at(timestamp, key)**
  - Delete the key at `timestamp`.
  - Return `True` if the key existed immediately before deletion, otherwise `False`.
- **get_at(timestamp, key)**
  - Return the value visible at `timestamp`.
  - If the key did not exist at that time, return `None`.
- **keys_at(timestamp, prefix)**
  - Return visible keys at `timestamp` that start with `prefix`, sorted lexicographically.

Timestamps passed to operations are non-decreasing.

### Examples

```python
store = TimeVersionedKV()
store.set_at(10, "a", "old")
store.set_at(20, "a", "new")
store.get_at(15, "a")        # "old"
store.get_at(20, "a")        # "new"
store.delete_at(30, "a")     # True
store.get_at(31, "a")        # None
```

