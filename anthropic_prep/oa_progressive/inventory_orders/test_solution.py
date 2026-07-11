import unittest
from solution import InventoryOrders


class TestInventoryOrders(unittest.TestCase):
    def test_level_1_inventory(self):
        store = InventoryOrders()
        self.assertTrue(store.add_product("book-1", "books", 25))
        self.assertFalse(store.add_product("book-1", "books", 30))
        self.assertEqual(store.restock("book-1", 10), 10)
        self.assertEqual(store.purchase("book-1", 3), 7)
        self.assertIsNone(store.purchase("book-1", 100))
        self.assertIsNone(store.restock("missing", 1))

    def test_level_2_aggregation(self):
        store = InventoryOrders()
        store.add_product("b", "books", 20)
        store.add_product("a", "books", 10)
        store.add_product("game", "games", 60)
        store.restock("a", 5)
        store.restock("b", 5)
        store.restock("game", 1)
        self.assertEqual(store.top_products("books", 2), ["a(5)", "b(5)"])
        self.assertEqual(store.inventory_value("books"), 150)

    def test_level_3_reservations(self):
        store = InventoryOrders()
        store.add_product("game", "games", 60)
        store.restock("game", 5)
        reservation_id = store.reserve_at(10, "game", 3, 5)
        self.assertEqual(reservation_id, "reservation1")
        self.assertIsNone(store.purchase_at(11, "game", 3))
        self.assertTrue(store.complete_reservation_at(12, reservation_id))
        self.assertEqual(store.purchase_at(13, "game", 2), 0)
        expired = store.reserve_at(20, "game", 0, 1)
        self.assertFalse(store.complete_reservation_at(21, expired))

    def test_level_4_discontinue_report(self):
        store = InventoryOrders()
        store.add_product("book", "books", 25)
        store.restock("book", 10)
        store.purchase("book", 4)
        self.assertEqual(store.sales_report("books"), ["book(4,100)"])
        self.assertTrue(store.discontinue("book"))
        self.assertIsNone(store.purchase("book", 1))
        self.assertFalse(store.discontinue("book"))


if __name__ == "__main__":
    unittest.main()

