# Scenario

Your task is to implement a simplified version of a build system.

## Level 1 - Initial Design & Basic Functions

- **add_target(target_id)**
- **touch(target_id)**
- **build(target_id)**
- **is_built(target_id)**

## Level 2 - Data Structures & Data Processing

- **add_dependency(target_id, dependency_id)**
- **build_order(target_id)**

## Level 3 - Refactoring & Encapsulation

The system should now reject dependency cycles and support recursive builds.

- **add_dependency_checked(target_id, dependency_id)**
  - Add a dependency only if it would not create a cycle.
  - Return `True` if the dependency was added.
  - Return `False` if either target is missing, the dependency already exists, or a cycle would be created.
- **build_with_dependencies(target_id)**
  - Build all unbuilt dependencies, then the target.
  - Return the targets that were actually built in build order.
  - Already built targets should not be included.
  - If the target does not exist or dependencies contain a cycle, return `[]`.

### Examples

```python
system = BuildSystem()
for target in ["app", "lib", "core"]:
    system.add_target(target)
system.add_dependency_checked("app", "lib")       # True
system.add_dependency_checked("lib", "core")      # True
system.add_dependency_checked("core", "app")      # False
system.build_with_dependencies("app")             # ["core", "lib", "app"]
system.build_with_dependencies("app")             # []
```

