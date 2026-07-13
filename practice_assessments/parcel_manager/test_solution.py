import importlib
import os
import unittest


ParcelManager = importlib.import_module(os.getenv("SOLUTION_MODULE", "solution")).ParcelManager


class TestParcelManager(unittest.TestCase):
    def test_level_1_inventory(self):
        manager = ParcelManager()
        self.assertTrue(manager.add_parcel("parcel-a", 10))
        self.assertFalse(manager.add_parcel("parcel-a", 20))
        self.assertFalse(manager.add_parcel("", 10))
        self.assertFalse(manager.add_parcel("parcel-b", 0))
        parcel = manager.get_parcel("parcel-a")
        self.assertEqual(parcel, {"size": 10, "status": "created"})
        parcel["status"] = "mutated"
        self.assertEqual(manager.get_parcel("parcel-a"), {"size": 10, "status": "created"})
        self.assertTrue(manager.remove_parcel("parcel-a"))
        self.assertFalse(manager.remove_parcel("parcel-a"))
        self.assertIsNone(manager.get_parcel("parcel-a"))

    def test_level_2_inventory_queries(self):
        manager = ParcelManager()
        manager.add_parcel("parcel-a", 10)
        manager.add_parcel("parcel-c", 20)
        manager.add_parcel("parcel-b", 20)
        manager.add_parcel("letter-a", 1)
        self.assertEqual(manager.find_parcels("parcel-"), ["parcel-a", "parcel-b", "parcel-c"])
        self.assertEqual(manager.find_parcels("missing"), [])
        self.assertEqual(
            manager.top_parcels(3),
            [("parcel-b", 20), ("parcel-c", 20), ("parcel-a", 10)],
        )
        self.assertEqual(manager.top_parcels(0), [])

    def test_level_3_courier_gated_status(self):
        manager = ParcelManager()
        manager.add_parcel("parcel-a", 10)
        self.assertFalse(manager.update_status("parcel-a", "in_transit"))
        self.assertTrue(manager.add_courier("courier-1"))
        self.assertFalse(manager.add_courier("courier-1"))
        self.assertFalse(manager.add_courier(""))
        self.assertFalse(manager.assign_courier("missing", "courier-1"))
        self.assertFalse(manager.assign_courier("parcel-a", "missing"))
        self.assertTrue(manager.assign_courier("parcel-a", "courier-1"))
        self.assertEqual(manager.assigned_courier("parcel-a"), "courier-1")
        self.assertTrue(manager.update_status("parcel-a", "in_transit"))
        self.assertFalse(manager.update_status("parcel-a", "in_transit"))
        self.assertEqual(manager.get_parcel("parcel-a"), {"size": 10, "status": "in_transit"})

    def test_level_4_version_rollback(self):
        manager = ParcelManager()
        manager.add_parcel("parcel-a", 10)       # version 1
        manager.add_parcel("parcel-b", 20)       # version 2
        manager.add_courier("courier-1")          # version 3
        manager.assign_courier("parcel-a", "courier-1")  # version 4
        manager.update_status("parcel-a", "in_transit")  # version 5
        self.assertTrue(manager.rollback(3))
        self.assertEqual(manager.get_parcel("parcel-a"), {"size": 10, "status": "created"})
        self.assertEqual(manager.assigned_courier("parcel-a"), None)
        self.assertEqual(manager.get_parcel("parcel-b"), {"size": 20, "status": "created"})
        self.assertTrue(manager.assign_courier("parcel-a", "courier-1"))
        self.assertFalse(manager.rollback(5))
        self.assertTrue(manager.rollback(0))
        self.assertIsNone(manager.get_parcel("parcel-a"))
        self.assertFalse(manager.assign_courier("parcel-a", "courier-1"))


if __name__ == "__main__":
    unittest.main()
