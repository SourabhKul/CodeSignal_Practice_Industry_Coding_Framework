# Scenario

Your task is to implement a simplified version of a build system.

## Level 1 - Initial Design & Basic Functions

- **add_target(target_id)**
- **touch(target_id)**
- **build(target_id)**
- **is_built(target_id)**

## Level 2 - Data Structures & Data Processing

Targets can now depend on other targets.

- **add_dependency(target_id, dependency_id)**
  - Add a dependency from `target_id` to `dependency_id`.
  - Return `True` if both targets exist and the dependency was added.
  - If either target does not exist, return `False`.
  - If the dependency already exists, return `False`.
- **build_order(target_id)**
  - Return the targets that should be built to build `target_id`, dependencies first.
  - Include `target_id` in the returned list.
  - If multiple dependencies can be built in any order, use lexicographical order.
  - If the target does not exist, return `[]`.

### Examples

```python
system = BuildSystem()
system.add_target("app")
system.add_target("lib")
system.add_target("core")
system.add_dependency("app", "lib")       # True
system.add_dependency("lib", "core")      # True
system.build_order("app")                 # ["core", "lib", "app"]
```

