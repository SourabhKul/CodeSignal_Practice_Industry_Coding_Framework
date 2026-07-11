# Scenario

Your task is to implement a simplified version of a package manager.

## Level 1 - Initial Design & Basic Functions

- **add_package(package_name)**
- **install(package_name)**
- **is_installed(package_name)**

## Level 2 - Data Structures & Data Processing

- **add_dependency(package_name, dependency_name)**
- **install_order(package_name)**

## Level 3 - Refactoring & Encapsulation

Dependencies can now be invalid if they create cycles.

- **add_dependency_checked(package_name, dependency_name)**
  - Add a dependency only if it would not create a cycle.
  - Return `True` if added.
  - Return `False` if either package is missing or the dependency would create a cycle.
- **install_with_dependencies(package_name)**
  - Install all dependencies and then the requested package.
  - Return the installation order.
  - Return `[]` if the package does not exist or dependencies contain a cycle.

