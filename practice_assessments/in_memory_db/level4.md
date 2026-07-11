# Scenario

Your task is to implement a simplified version of an in-memory database.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
run tests often and receive partial credit for passed tests. Please check tests for requirements and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, not all together, keeping in mind that you will need to refactor to support additional functionality.
Please, do not change the existing method signatures.

## Level 1 - Initial Design & Basic Functions

- **set(key, field, value)**
- **get(key, field)**
- **delete(key, field)**

## Level 2 - Data Structures & Data Processing

- **scan(key)**
- **scan_by_prefix(key, prefix)**

## Level 3 - Refactoring & Encapsulation

- **set_at(key, field, value, timestamp)**
- **set_at_with_ttl(key, field, value, timestamp, ttl)**
- **get_at(key, field, timestamp)**
- **delete_at(key, field, timestamp)**
- **scan_at(key, timestamp)**
- **scan_by_prefix_at(key, prefix, timestamp)**

## Level 4 - Extending Design & Functionality

- **backup(timestamp)**
  - Save a snapshot of fields alive at `timestamp`.
  - Return the number of records that contain at least one live field.
- **restore(timestamp, restore_to)**
  - Restore the latest backup whose backup timestamp is less than or equal to `restore_to`.
  - Return `None`.
  - TTL fields should keep the same remaining lifetime they had at backup time, counted from the restore timestamp.

### Examples

```python
db = InMemoryDB()
db.set_at_with_ttl("a", "x", "1", 10, 10) # expires at 20
db.set_at("b", "z", "9", 11)
db.backup(15)                             # 2
db.set_at("a", "x", "changed", 16)
db.restore(18, 15)                        # None
db.get_at("a", "x", 22)                   # "1"
db.get_at("a", "x", 23)                   # None
```

