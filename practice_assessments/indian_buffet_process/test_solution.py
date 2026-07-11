import importlib
import os
import unittest
from fractions import Fraction


IndianBuffet = importlib.import_module(os.getenv("SOLUTION_MODULE", "solution")).IndianBuffet


class TestIndianBuffet(unittest.TestCase):
    def seed_buffet(self):
        buffet = IndianBuffet(3)
        self.assertEqual(buffet.add_customer([], 2), [1, 2])
        self.assertEqual(buffet.add_customer([0, 0], 1), [1, 2, 3])
        self.assertEqual(buffet.add_customer([1, 0, 1], 0), [1, 2])
        return buffet

    def test_level_1_sampling(self):
        buffet = self.seed_buffet()
        self.assertEqual(buffet.customer_dishes(1), [1, 2])
        self.assertEqual(buffet.customer_dishes(2), [1, 2, 3])
        self.assertEqual(buffet.dish_popularity(1), 3)
        self.assertEqual(buffet.dish_popularity(2), 3)
        self.assertEqual(buffet.dish_popularity(3), 1)
        self.assertIsNone(buffet.add_customer([3, 0, 0], 0))
        self.assertEqual(buffet.customer_dishes(4), None)
        self.assertEqual(buffet.dish_popularity(4), 0)

    def test_level_2_matrix_and_popularity(self):
        buffet = self.seed_buffet()
        self.assertEqual(buffet.feature_matrix(), [[1, 1, 0], [1, 1, 1], [1, 1, 0]])
        self.assertEqual(buffet.popular_dishes(2), [(1, 3), (2, 3)])
        self.assertEqual(buffet.popular_dishes(0), [])
        self.assertEqual(buffet.expected_new_dishes(), Fraction(3, 4))

    def test_level_3_customer_tags(self):
        buffet = self.seed_buffet()
        self.assertTrue(buffet.add_tag(1, "research"))
        self.assertFalse(buffet.add_tag(1, "research"))
        self.assertTrue(buffet.add_tag(3, "research"))
        self.assertFalse(buffet.add_tag(4, "research"))
        self.assertEqual(buffet.customers_with_tag("research"), [1, 3])
        self.assertEqual(buffet.recommend_dishes(1, 3), [3])
        self.assertEqual(buffet.recommend_dishes(1, 0), [])
        self.assertIsNone(buffet.recommend_dishes(4, 1))

    def test_level_4_snapshots(self):
        buffet = self.seed_buffet()
        buffet.add_tag(1, "research")
        self.assertTrue(buffet.save("base"))
        self.assertFalse(buffet.save("base"))
        self.assertEqual(buffet.add_customer([2, 1, 0], 1), [1, 2, 3, 4])
        self.assertTrue(buffet.add_tag(4, "new"))
        self.assertTrue(buffet.restore("base"))
        self.assertEqual(buffet.feature_matrix(), [[1, 1, 0], [1, 1, 1], [1, 1, 0]])
        self.assertEqual(buffet.customers_with_tag("research"), [1])
        self.assertEqual(buffet.customers_with_tag("new"), [])
        self.assertEqual(buffet.add_customer([2, 1, 0], 0), [1, 2, 3])
        self.assertFalse(buffet.restore("missing"))


if __name__ == "__main__":
    unittest.main()

