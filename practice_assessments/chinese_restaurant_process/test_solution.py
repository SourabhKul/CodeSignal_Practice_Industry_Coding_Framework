import importlib
import os
import unittest


ChineseRestaurant = importlib.import_module(
    os.getenv("SOLUTION_MODULE", "solution")
).ChineseRestaurant


class TestChineseRestaurant(unittest.TestCase):
    def test_level_1_seating(self):
        restaurant = ChineseRestaurant(2)
        self.assertEqual(restaurant.customer_table(1), 1)
        self.assertEqual(restaurant.table_size(1), 1)
        self.assertEqual(restaurant.seat(0), 2)
        self.assertEqual(restaurant.seat(2), 1)
        self.assertEqual(restaurant.seat(4), 1)
        self.assertEqual(restaurant.seat(1), 3)
        self.assertEqual(
            [restaurant.customer_table(i) for i in range(1, 6)],
            [1, 2, 1, 1, 3],
        )
        self.assertEqual(restaurant.table_size(1), 3)
        self.assertIsNone(restaurant.seat(7))
        self.assertIsNone(restaurant.customer_table(6))
        self.assertEqual(restaurant.table_size(4), 0)

    def test_level_2_bulk_and_ranking(self):
        restaurant = ChineseRestaurant(2)
        self.assertEqual(restaurant.seat_many([0, 99, 2, 4, 1]), [2, None, 1, 1, 3])
        self.assertEqual(restaurant.list_tables(), [(1, 3), (2, 1), (3, 1)])
        self.assertEqual(restaurant.customer_table(5), 3)

    def test_level_3_snapshots(self):
        restaurant = ChineseRestaurant(2)
        restaurant.seat_many([0, 2])
        self.assertTrue(restaurant.save("early"))
        self.assertFalse(restaurant.save("early"))
        restaurant.seat_many([1, 4])
        self.assertEqual(restaurant.list_tables(), [(1, 3), (2, 1), (3, 1)])
        self.assertTrue(restaurant.restore("early"))
        self.assertEqual(restaurant.list_tables(), [(1, 2), (2, 1)])
        self.assertEqual(restaurant.seat(1), 3)
        self.assertFalse(restaurant.restore("missing"))
        self.assertTrue(restaurant.delete_snapshot("early"))
        self.assertFalse(restaurant.delete_snapshot("early"))

    def test_level_4_forks(self):
        restaurant = ChineseRestaurant(2)
        restaurant.seat_many([0, 2])
        restaurant.save("early")
        restaurant.seat_many([1, 4])
        restaurant.save("late")

        self.assertEqual(
            restaurant.compare_snapshots("early", "late"),
            [(1, 1), (3, 1)],
        )
        self.assertIsNone(restaurant.compare_snapshots("early", "missing"))

        forked = restaurant.fork("early")
        self.assertIsNotNone(forked)
        self.assertEqual(forked.list_tables(), [(1, 2), (2, 1)])
        self.assertEqual(forked.seat(1), 3)
        self.assertEqual(forked.list_tables(), [(1, 2), (2, 1), (3, 1)])
        self.assertEqual(restaurant.list_tables(), [(1, 3), (2, 1), (3, 1)])
        self.assertFalse(forked.restore("early"))
        self.assertIsNone(restaurant.fork("missing"))


if __name__ == "__main__":
    unittest.main()
