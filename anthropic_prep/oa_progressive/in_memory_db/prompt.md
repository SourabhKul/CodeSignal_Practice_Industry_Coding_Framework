# OA Drill: In-Memory Database

Implement `InMemoryDB` in `solution.py`.

All keys, fields, and values are strings. Timestamps and TTLs are integers. Methods should not print anything.

## Level 1

- `set(key, field, value)` stores a string value.
  - If the record or field already exists, overwrite the existing value.
  - Return `None`.
- `get(key, field)` returns the value or `None`.
- `delete(key, field)` removes a field and returns `True` if it existed, otherwise `False`.

Example:

```python
db = InMemoryDB()
db.set("user1", "name", "Ada")      # None
db.set("user1", "city", "London")   # None
db.get("user1", "name")             # "Ada"
db.get("user1", "age")              # None
db.delete("user1", "city")          # True
db.delete("user1", "city")          # False
db.get("missing", "name")           # None
```

## Level 2

- `scan(key)` returns all fields for `key` as `["field(value)", ...]`, sorted lexicographically by field.
- `scan_by_prefix(key, prefix)` returns only fields that start with `prefix`, same format and sort.
- Return `[]` if the key does not exist or no fields match.

Example:

```python
db = InMemoryDB()
db.set("user1", "name", "Ada")
db.set("user1", "nickname", "ace")
db.set("user1", "city", "London")

db.scan("user1")
# ["city(London)", "name(Ada)", "nickname(ace)"]

db.scan_by_prefix("user1", "ni")
# ["nickname(ace)"]

db.scan_by_prefix("user1", "missing")
# []

db.scan("missing")
# []
```

## Level 3

Add timestamped operations:

- `set_at(key, field, value, timestamp)`
- `set_at_with_ttl(key, field, value, timestamp, ttl)`
- `get_at(key, field, timestamp)`
- `delete_at(key, field, timestamp)`
- `scan_at(key, timestamp)`
- `scan_by_prefix_at(key, prefix, timestamp)`

Timestamped methods should behave like their non-timestamped versions, but only consider values that are alive at the provided timestamp.

A TTL entry is alive for timestamps `created_timestamp <= t < created_timestamp + ttl`. At exactly `created_timestamp + ttl`, it is expired.

A non-TTL entry never expires unless overwritten or deleted.

If a field is overwritten, the new value and expiration replace the old value.

Examples:

```python
db = InMemoryDB()
db.set_at_with_ttl("a", "x", "1", 10, 5)  # alive at 10, 11, 12, 13, 14
db.get_at("a", "x", 10)                   # "1"
db.get_at("a", "x", 14)                   # "1"
db.get_at("a", "x", 15)                   # None

db.set_at("a", "y", "2", 11)
db.scan_at("a", 14)                       # ["x(1)", "y(2)"]
db.scan_at("a", 15)                       # ["y(2)"]

db.delete_at("a", "y", 16)                # True
db.get_at("a", "y", 17)                   # None
db.delete_at("a", "missing", 18)          # False
```

## Level 4

- `backup(timestamp)` saves the live database state at `timestamp` and returns the number of non-empty records.
- `restore(timestamp, restore_to)` restores the latest backup at or before `restore_to`.

When restoring TTL records, preserve their remaining lifetime relative to the restore timestamp.

More precisely:

- `backup(timestamp)` stores only fields alive at `timestamp`.
- Its return value is the number of keys that have at least one live field.
- `restore(timestamp, restore_to)` finds the latest backup whose backup time is `<= restore_to`.
- After restore, TTL fields should expire after the same remaining duration they had at backup time, counted from `timestamp`.
- `restore` returns `None`.

Example:

```python
db = InMemoryDB()
db.set_at_with_ttl("a", "x", "1", 10, 10) # expires at 20
db.set_at("b", "z", "9", 11)

db.backup(15)                             # 2
# At backup time, a.x has 5 seconds remaining.

db.set_at("a", "x", "changed", 16)
db.restore(18, 15)                        # None

db.get_at("a", "x", 19)                   # "1"
db.get_at("a", "x", 22)                   # "1"
db.get_at("a", "x", 23)                   # None
db.get_at("b", "z", 100)                  # "9"
```
