# Scenario

Your task is to implement a simplified version of a key-value store.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
run tests often and receive partial credit for passed tests. Please check tests for requirements and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, not all together, keeping in mind that you will need to refactor to support additional functionality.
Please, do not change the existing method signatures.

## Level 1 - Initial Design & Basic Functions

- **set(key, value)**
  - Store `value` for `key`.
  - If the key already exists, overwrite the value.
  - Return `None`.
- **get(key)**
  - Return the current value for `key`.
  - If the key does not exist, return `None`.
- **delete(key)**
  - Delete the key.
  - Return `True` if the key existed, otherwise `False`.

### Examples

```python
store = TimeVersionedKV()
store.set("mode", "fast")      # None
store.get("mode")              # "fast"
store.delete("mode")           # True
store.get("mode")              # None
```

