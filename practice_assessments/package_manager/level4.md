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

- **add_dependency_checked(package_name, dependency_name)**
- **install_with_dependencies(package_name)**

## Level 4 - Extending Design & Functionality

- **remove_package(package_name)**
  - Remove an installed package if no installed package depends on it.
  - Return `True` if removed, otherwise `False`.
- **dependents(package_name)**
  - Return installed packages that directly or indirectly depend on `package_name`.
  - Order lexicographically.

