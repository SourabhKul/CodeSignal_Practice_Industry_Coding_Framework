# Scenario

Your task is to implement a simplified version of an in-memory database.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
run tests often and receive partial credit for passed tests. Please check tests for requirements and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, not all together, keeping in mind that you will need to refactor to support additional functionality.
Please, do not change the existing method signatures.

## Task

The database stores string values in records. Each record is identified by a string `key`, and each value inside a
record is identified by a string `field`.

## Level 1 - Initial Design & Basic Functions

- **set(key, field, value)**
- **get(key, field)**
- **delete(key, field)**

## Level 2 - Data Structures & Data Processing

- **scan(key)**
  - Return all fields for `key` in the format `["field(value)", ...]`.
  - Results should be sorted by field in ascending lexicographical order.
  - Return `[]` if the key does not exist.
- **scan_by_prefix(key, prefix)**
  - Return all fields for `key` whose field names start with `prefix`.
  - Use the same format and ordering as `scan`.
  - Return `[]` if the key does not exist or no fields match.

### Examples

```python
db = InMemoryDB()
db.set("user1", "name", "Ada")
db.set("user1", "nickname", "ace")
db.set("user1", "city", "London")

db.scan("user1")
# ["city(London)", "name(Ada)", "nickname(ace)"]

db.scan_by_prefix("user1", "ni")
# ["nickname(ace)"]

db.scan("missing")
# []
```

