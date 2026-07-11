# Live Drill: Persistent Thread-Safe LRU Cache

Implement `PersistentLRUCache`.

Requirements:

- `get(key)` returns value or `None`.
- `put(key, value)` stores and marks the key most recently used.
- Evict the least recently used item when capacity is exceeded.
- Operations must be thread-safe.
- `save()` persists state to disk.
- `load()` restores state from disk.

Talk through crash-safety improvements: temp file, fsync, atomic rename.

