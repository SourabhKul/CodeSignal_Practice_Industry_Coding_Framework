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

- **set_at(timestamp, key, value)**
- **delete_at(timestamp, key)**
- **get_at(timestamp, key)**
- **keys_at(timestamp, prefix)**

## Level 4 - Extending Design & Functionality

The store now supports compaction.

- **compact(timestamp)**
  - Remove historical versions that cannot affect any future `get_at` query at or after `timestamp`.
  - Keep enough information to answer `get_at(timestamp, key)` and later queries correctly.
  - Return the number of historical entries removed.
- **history(key)**
  - Return the remaining history for `key` as `["timestamp(value)", ...]`.
  - Deleted versions should be represented as `"timestamp(<deleted>)"`.

### Examples

```python
store = TimeVersionedKV()
store.set_at(10, "a", "old")
store.set_at(20, "a", "new")
store.compact(15)            # 0
store.compact(20)            # 1
store.get_at(20, "a")        # "new"
store.history("a")           # ["20(new)"]
```

