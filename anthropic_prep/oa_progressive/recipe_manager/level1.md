# Scenario

Implement an in-memory recipe manager. Recipe names are unique case-insensitively, while returned names preserve their original spelling.

## Level 1 - Initial Design & Basic Functions

- **add_recipe(name, ingredients)**
  - Add a recipe whose ingredients are supplied as a list of strings.
  - Return `False` if the name already exists case-insensitively; otherwise return `True`.
- **get_recipe(name)**
  - Return a copy of the ingredient list, or `None` when absent.
- **update_recipe(name, ingredients)**
  - Replace the ingredients and return `True`, or return `False` when absent.

Do not expose mutable internal lists to callers.
