from copy import deepcopy


class RecipeManager:
    def __init__(self):
        self.recipes = {}
        self.users = set()

    def _key(self, name):
        return name.casefold()

    def _append_version(self, recipe, ingredients):
        recipe["ingredients"] = list(ingredients)
        recipe["history"].append(list(ingredients))

    def add_recipe(self, name, ingredients):
        key = self._key(name)
        if key in self.recipes:
            return False
        self.recipes[key] = {
            "name": name,
            "ingredients": list(ingredients),
            "history": [list(ingredients)],
            "owner": None,
            "editors": set(),
        }
        return True

    def get_recipe(self, name):
        recipe = self.recipes.get(self._key(name))
        return None if recipe is None else list(recipe["ingredients"])

    def update_recipe(self, name, ingredients):
        recipe = self.recipes.get(self._key(name))
        if recipe is None:
            return False
        self._append_version(recipe, ingredients)
        return True

    def _ordered(self, recipes):
        return [
            recipe["name"]
            for recipe in sorted(recipes, key=lambda recipe: (-len(recipe["ingredients"]), recipe["name"].casefold()))
        ]

    def list_recipes(self):
        return self._ordered(self.recipes.values())

    def search_by_ingredient(self, ingredient):
        needle = ingredient.casefold()
        return self._ordered(
            recipe
            for recipe in self.recipes.values()
            if any(item.casefold() == needle for item in recipe["ingredients"])
        )

    def add_user(self, user_id):
        if user_id in self.users:
            return False
        self.users.add(user_id)
        return True

    def add_recipe_by(self, user_id, name, ingredients):
        if user_id not in self.users or not self.add_recipe(name, ingredients):
            return False
        recipe = self.recipes[self._key(name)]
        recipe["owner"] = user_id
        recipe["editors"].add(user_id)
        return True

    def grant_editor(self, owner_id, recipe_name, editor_id):
        recipe = self.recipes.get(self._key(recipe_name))
        if recipe is None or recipe["owner"] != owner_id or editor_id not in self.users:
            return False
        recipe["editors"].add(editor_id)
        return True

    def update_recipe_by(self, user_id, recipe_name, ingredients):
        recipe = self.recipes.get(self._key(recipe_name))
        if recipe is None or user_id not in recipe["editors"]:
            return False
        self._append_version(recipe, ingredients)
        return True

    def history(self, name):
        recipe = self.recipes.get(self._key(name))
        return [] if recipe is None else deepcopy(recipe["history"])

    def rollback(self, name, version):
        recipe = self.recipes.get(self._key(name))
        if recipe is None or version < 1 or version > len(recipe["history"]):
            return False
        self._append_version(recipe, recipe["history"][version - 1])
        return True
