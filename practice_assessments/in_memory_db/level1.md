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

Example of database state:

```plaintext
[database]
    +- user1
    |   +- city = London
    |   +- name = Ada
    +- user2
        +- name = Grace
```

## Level 1 - Initial Design & Basic Functions

- **set(key, field, value)**
  - Store `value` in `field` for `key`.
  - If the record or field already exists, overwrite the existing value.
  - Return `None`.
- **get(key, field)**
  - Return the value stored at `key.field`.
  - If the key or field does not exist, return `None`.
- **delete(key, field)**
  - Delete the field from the record.
  - Return `True` if the field existed and was deleted.
  - Otherwise, return `False`.

### Examples

```python
db = InMemoryDB()
db.set("user1", "name", "Ada")      # None
db.get("user1", "name")             # "Ada"
db.get("user1", "age")              # None
db.delete("user1", "name")          # True
db.delete("user1", "name")          # False
```

