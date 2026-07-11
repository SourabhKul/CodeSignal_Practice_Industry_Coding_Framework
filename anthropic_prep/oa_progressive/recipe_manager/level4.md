# Scenario

Implement an in-memory recipe manager. All previous behavior remains valid.

## Level 1 - Initial Design & Basic Functions

- **add_recipe(name, ingredients)**
- **get_recipe(name)**
- **update_recipe(name, ingredients)**

## Level 2 - Data Structures & Data Processing

- **list_recipes()**
- **search_by_ingredient(ingredient)**

## Level 3 - Refactoring & Encapsulation

- **add_user(user_id)**
- **add_recipe_by(user_id, name, ingredients)**
- **grant_editor(owner_id, recipe_name, editor_id)**
- **update_recipe_by(user_id, recipe_name, ingredients)**

## Level 4 - Extending Design & Functionality

- **history(name)**
  - Return copies of every ingredient-list version from oldest to newest.
  - Return `[]` when the recipe does not exist.
- **rollback(name, version)**
  - Restore a one-based historical version and append the restored state as a new version.
  - Return `True` on success and `False` for a missing recipe or invalid version.
