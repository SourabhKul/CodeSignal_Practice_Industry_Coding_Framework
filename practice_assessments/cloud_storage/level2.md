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
  - Return at most 10 files whose names start with `prefix` and end with `suffix`.
  - Order files by size in descending order.
  - If sizes tie, order by file name in ascending lexicographical order.
  - Return values in the format `["name(size)", ...]`.
  - Return `[]` if no files match.

### Examples

```python
storage = CloudStorage()
storage.add_file("/docs/a.txt", 100)
storage.add_file("/docs/b.txt", 200)
storage.add_file("/img/a.png", 300)
storage.find_file("/docs", ".txt")
# ["/docs/b.txt(200)", "/docs/a.txt(100)"]
```

