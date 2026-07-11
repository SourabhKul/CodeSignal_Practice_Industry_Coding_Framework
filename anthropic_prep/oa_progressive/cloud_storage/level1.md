# Scenario

Your task is to implement a simplified version of a cloud storage system.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
run tests often and receive partial credit for passed tests. Please check tests for requirements and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, not all together, keeping in mind that you will need to refactor to support additional functionality.
Please, do not change the existing method signatures.

## Task

The cloud storage system stores files in memory. Each file has a name and size in bytes.

Example of storage state:

```plaintext
[storage]
    +- /docs/readme.txt 120
    +- /media/photo.png 700
```

## Level 1 - Initial Design & Basic Functions

- **add_file(name, size)**
  - Add a file with the specified name and size.
  - Return `True` if the file was added.
  - If a file with the same name already exists, return `False`.
- **copy_file(source, dest)**
  - Copy the source file to destination.
  - Return `True` if the copy succeeded.
  - If the source file does not exist, return `False`.
  - If the destination already exists, return `False`.
- **get_file_size(name)**
  - Return the file size.
  - If the file does not exist, return `None`.

### Examples

```python
storage = CloudStorage()
storage.add_file("/a.txt", 100)        # True
storage.add_file("/a.txt", 200)        # False
storage.copy_file("/a.txt", "/b.txt")  # True
storage.get_file_size("/b.txt")        # 100
storage.copy_file("/x.txt", "/y.txt")  # False
```

