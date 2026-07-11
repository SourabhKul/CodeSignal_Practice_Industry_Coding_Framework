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

Records can now be written and queried at a specific timestamp. Implement extensions of existing methods which
inherit all functionality but also include a timestamp. New writes might specify a time to live.

- **set_at(key, field, value, timestamp)**
- **set_at_with_ttl(key, field, value, timestamp, ttl)**
  - Store the value for `ttl` seconds.
  - The value is alive for timestamps `timestamp <= t < timestamp + ttl`.
- **get_at(key, field, timestamp)**
- **delete_at(key, field, timestamp)**
- **scan_at(key, timestamp)**
- **scan_by_prefix_at(key, prefix, timestamp)**

Timestamped operations only consider fields that are alive at the provided timestamp. Non-TTL values live forever
unless overwritten or deleted.

### Examples

```python
db = InMemoryDB()
db.set_at_with_ttl("a", "x", "1", 10, 5)
db.get_at("a", "x", 14)             # "1"
db.get_at("a", "x", 15)             # None
db.set_at("a", "y", "2", 11)
db.scan_at("a", 14)                 # ["x(1)", "y(2)"]
db.scan_at("a", 15)                 # ["y(2)"]
```

