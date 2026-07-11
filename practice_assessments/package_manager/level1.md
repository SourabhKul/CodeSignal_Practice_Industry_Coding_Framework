# Scenario

Your task is to implement a simplified version of a package manager.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
run tests often and receive partial credit for passed tests. Please check tests for requirements and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, not all together, keeping in mind that you will need to refactor to support additional functionality.
Please, do not change the existing method signatures.

## Level 1 - Initial Design & Basic Functions

- **add_package(package_name)**
  - Add a package with no dependencies.
  - Return `True` if added, otherwise `False`.
- **install(package_name)**
  - Install the package.
  - Return `True` if installed or already installed.
  - If the package does not exist, return `False`.
- **is_installed(package_name)**
  - Return `True` if installed, otherwise `False`.

