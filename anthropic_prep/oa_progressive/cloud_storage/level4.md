# Scenario

Your task is to implement a simplified version of a cloud storage system.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
run tests often and receive partial credit for passed tests. Please check tests for requirements and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, not all together, keeping in mind that you will need to refactor to support additional functionality.
Please, do not change the existing method signatures.

## Level 1 - Initial Design & Basic Functions

- **add_file(name, size)**
- **copy_file(source, dest)**
- **get_file_size(name)**

## Level 2 - Data Structures & Data Processing

- **find_file(prefix, suffix)**

## Level 3 - Refactoring & Encapsulation

- **add_user(user_id, capacity)**
- **add_file_by(user_id, name, size)**
- **copy_file_by(user_id, source, dest)**
- **update_capacity(user_id, capacity)**

## Level 4 - Extending Design & Functionality

- **backup_user(user_id)**
  - Save a snapshot of all files owned by the user.
  - Return the number of backed up files.
  - If the user does not exist, return `None`.
- **restore_user(user_id)**
  - Restore the latest backup for the user.
  - Return the number of restored files.
  - Files currently owned by the user that are not in the backup should be removed.
  - If a backed-up file name is currently used by another user, skip restoring that file.
  - If the user exists but has no backup, remove all files owned by the user and return `0`.
  - If the user does not exist, return `None`.

### Examples

```python
storage = CloudStorage()
storage.add_user("u1", 1000)
storage.add_file_by("u1", "/a.txt", 100)
storage.add_file_by("u1", "/b.txt", 200)
storage.backup_user("u1")                  # 2
storage.add_file_by("u1", "/c.txt", 300)
storage.restore_user("u1")                 # 2
storage.get_file_size("/c.txt")            # None
```

