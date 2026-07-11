# Scenario

Implement an in-memory recipe manager. All Level 1 behavior remains valid.

## Level 1 - Initial Design & Basic Functions

- **add_recipe(name, ingredients)**
- **get_recipe(name)**
- **update_recipe(name, ingredients)**

## Level 2 - Data Structures & Data Processing

- **list_recipes()**
  - Return recipe names ordered by ingredient count descending, then name case-insensitively ascending.
- **search_by_ingredient(ingredient)**
  - Return recipes containing the ingredient using a case-insensitive exact match.
  - Use the same ordering as `list_recipes()`.
