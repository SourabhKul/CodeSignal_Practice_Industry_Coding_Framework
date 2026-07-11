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

The storage now supports users with capacity limits. Existing files from Level 1 belong to an admin user with
unlimited capacity.

- **add_user(user_id, capacity)**
  - Add a user with the specified capacity.
  - Return `True` if the user was added, otherwise `False`.
- **add_file_by(user_id, name, size)**
  - Add a file owned by `user_id`.
  - Return the user's remaining capacity if the file was added.
  - If the user does not exist, the file already exists, or the file would exceed capacity, return `None`.
- **copy_file_by(user_id, source, dest)**
  - Copy a file owned by `user_id`.
  - Return the user's remaining capacity if the copy succeeded.
  - If the source does not exist, destination exists, owner is different, or capacity is exceeded, return `None`.
- **update_capacity(user_id, capacity)**
  - Update a user's capacity.
  - If the new capacity is lower than current usage, remove that user's largest files until usage is within capacity.
  - If sizes tie, remove lexicographically largest file names first.
  - Return the number of removed files, or `None` if the user does not exist.

### Examples

```python
storage = CloudStorage()
storage.add_user("u1", 500)                 # True
storage.add_file_by("u1", "/a.txt", 200)    # 300
storage.add_file_by("u1", "/b.txt", 400)    # None
storage.copy_file_by("u1", "/a.txt", "/c")  # 100
storage.update_capacity("u1", 250)          # 1
```

