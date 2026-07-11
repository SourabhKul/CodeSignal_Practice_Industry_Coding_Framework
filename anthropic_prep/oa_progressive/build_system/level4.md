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

- **add_dependency_checked(target_id, dependency_id)**
- **build_with_dependencies(target_id)**

## Level 4 - Extending Design & Functionality

When a target changes, every target that directly or indirectly depends on it becomes stale.

- **touch_cascade(target_id)**
  - Increment the target's source version.
  - Mark the target and all direct or indirect dependents as not built.
  - Return the stale targets sorted lexicographically.
  - If the target does not exist, return `[]`.
- **stale_targets()**
  - Return all existing targets that are not currently built, sorted lexicographically.

### Examples

```python
system = BuildSystem()
for target in ["app", "lib", "core"]:
    system.add_target(target)
system.add_dependency_checked("app", "lib")
system.add_dependency_checked("lib", "core")
system.build_with_dependencies("app")      # ["core", "lib", "app"]
system.touch_cascade("core")               # ["app", "core", "lib"]
system.stale_targets()                     # ["app", "core", "lib"]
```

