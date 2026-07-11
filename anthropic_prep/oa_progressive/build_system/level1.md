# Scenario

Your task is to implement a simplified version of a build system.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
run tests often and receive partial credit for passed tests. Please check tests for requirements and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, not all together, keeping in mind that you will need to refactor to support additional functionality.
Please, do not change the existing method signatures.

## Task

The build system stores targets, their versions, and later dependencies between targets.

Example of build state:

```plaintext
[build]
    +- lib     version=1  built=False
    +- app     version=1  built=False
```

## Level 1 - Initial Design & Basic Functions

- **add_target(target_id)**
  - Add a target with source version `1`.
  - Return `True` if the target was added.
  - If the target already exists, return `False`.
- **touch(target_id)**
  - Increment the target's source version.
  - Mark the target as not built.
  - Return the new source version.
  - If the target does not exist, return `None`.
- **build(target_id)**
  - Build the target.
  - Return `True` if the target exists and was built.
  - If the target does not exist, return `False`.
- **is_built(target_id)**
  - Return `True` if the target exists and is currently built.
  - Otherwise, return `False`.

### Examples

```python
system = BuildSystem()
system.add_target("app")      # True
system.add_target("app")      # False
system.is_built("app")        # False
system.build("app")           # True
system.is_built("app")        # True
system.touch("app")           # 2
system.is_built("app")        # False
```

