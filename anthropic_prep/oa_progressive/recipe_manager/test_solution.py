import importlib
import os
import unittest


RecipeManager = importlib.import_module(os.getenv("SOLUTION_MODULE", "solution")).RecipeManager


class TestRecipeManager(unittest.TestCase):
    def test_level_1_recipes(self):
        manager = RecipeManager()
        self.assertTrue(manager.add_recipe("Pasta", ["noodles", "tomato"]))
        self.assertFalse(manager.add_recipe("pAsTa", ["cream"]))
        ingredients = manager.get_recipe("PASTA")
        self.assertEqual(ingredients, ["noodles", "tomato"])
        ingredients.append("mutated")
        self.assertEqual(manager.get_recipe("pasta"), ["noodles", "tomato"])
        self.assertTrue(manager.update_recipe("pasta", ["noodles", "pesto"]))
        self.assertEqual(manager.get_recipe("Pasta"), ["noodles", "pesto"])
        self.assertFalse(manager.update_recipe("missing", []))
        self.assertIsNone(manager.get_recipe("missing"))

    def test_level_2_search(self):
        manager = RecipeManager()
        manager.add_recipe("Toast", ["bread", "butter"])
        manager.add_recipe("Big Salad", ["lettuce", "tomato", "butter"])
        manager.add_recipe("Apple", ["fruit"])
        self.assertEqual(manager.list_recipes(), ["Big Salad", "Toast", "Apple"])
        self.assertEqual(manager.search_by_ingredient("BUTTER"), ["Big Salad", "Toast"])
        self.assertEqual(manager.search_by_ingredient("missing"), [])

    def test_level_3_users(self):
        manager = RecipeManager()
        self.assertTrue(manager.add_user("owner"))
        self.assertTrue(manager.add_user("editor"))
        self.assertFalse(manager.add_user("owner"))
        self.assertFalse(manager.add_recipe_by("missing", "Soup", ["water"]))
        self.assertTrue(manager.add_recipe_by("owner", "Soup", ["water", "salt"]))
        self.assertFalse(manager.update_recipe_by("editor", "Soup", ["stock"]))
        self.assertFalse(manager.grant_editor("editor", "Soup", "owner"))
        self.assertTrue(manager.grant_editor("owner", "Soup", "editor"))
        self.assertTrue(manager.update_recipe_by("editor", "Soup", ["stock", "salt"]))
        self.assertEqual(manager.get_recipe("Soup"), ["stock", "salt"])

    def test_level_4_history(self):
        manager = RecipeManager()
        manager.add_recipe("Soup", ["water"])
        manager.update_recipe("Soup", ["stock"])
        manager.update_recipe("Soup", ["stock", "salt"])
        self.assertEqual(manager.history("soup"), [["water"], ["stock"], ["stock", "salt"]])
        self.assertTrue(manager.rollback("Soup", 1))
        self.assertEqual(manager.get_recipe("Soup"), ["water"])
        self.assertEqual(manager.history("Soup")[-1], ["water"])
        self.assertFalse(manager.rollback("Soup", 0))
        self.assertFalse(manager.rollback("missing", 1))
        self.assertEqual(manager.history("missing"), [])


if __name__ == "__main__":
    unittest.main()
