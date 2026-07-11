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

The manager now supports users and recipe edit permissions.

- **add_user(user_id)**
  - Return `False` if the user exists; otherwise add the user and return `True`.
- **add_recipe_by(user_id, name, ingredients)**
  - Create a recipe owned by `user_id`; the owner can edit it.
  - Return `False` for a missing user or duplicate recipe name.
- **grant_editor(owner_id, recipe_name, editor_id)**
  - Grant edit access and return `True` only when both users exist and `owner_id` owns the recipe.
- **update_recipe_by(user_id, recipe_name, ingredients)**
  - Update only when `user_id` is an authorized editor; otherwise return `False`.

Recipes created with the Level 1 API are system-owned and cannot be changed through user APIs.
