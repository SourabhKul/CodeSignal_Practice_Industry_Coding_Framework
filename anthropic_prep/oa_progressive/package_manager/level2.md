# Scenario

Your task is to implement a simplified version of a package manager.

## Level 1 - Initial Design & Basic Functions

- **add_package(package_name)**
- **install(package_name)**
- **is_installed(package_name)**

## Level 2 - Data Structures & Data Processing

- **add_dependency(package_name, dependency_name)**
  - Add a dependency relation.
  - Return `True` if both packages exist and the dependency was added.
  - Return `False` otherwise.
- **install_order(package_name)**
  - Return the packages that must be installed to install `package_name`, dependencies first.
  - Include already installed packages in the order.
  - Return `[]` if the package does not exist.
  - If multiple dependencies can be installed in any order, use lexicographical order.

