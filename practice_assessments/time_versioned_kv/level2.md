# Scenario

Your task is to implement a simplified version of a key-value store.

## Level 1 - Initial Design & Basic Functions

- **set(key, value)**
- **get(key)**
- **delete(key)**

## Level 2 - Data Structures & Data Processing

- **keys(prefix)**
  - Return all current keys that start with `prefix`, sorted lexicographically.
  - Return `[]` if no keys match.
- **count(prefix)**
  - Return the number of current keys that start with `prefix`.

### Examples

```python
store = TimeVersionedKV()
store.set("user:1", "Ada")
store.set("user:2", "Grace")
store.set("team:1", "Infra")
store.keys("user:")          # ["user:1", "user:2"]
store.count("user:")         # 2
```

