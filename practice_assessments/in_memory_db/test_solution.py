import importlib
import os
import unittest


InMemoryDB = importlib.import_module(os.getenv("SOLUTION_MODULE", "solution")).InMemoryDB


class TestInMemoryDB(unittest.TestCase):
    def test_level_1_crud(self):
        db = InMemoryDB()
        self.assertIsNone(db.set("user1", "name", "Ada"))
        self.assertIsNone(db.set("user1", "city", "London"))
        self.assertEqual(db.get("user1", "name"), "Ada")
        self.assertIsNone(db.get("user1", "missing"))
        self.assertTrue(db.delete("user1", "city"))
        self.assertFalse(db.delete("user1", "city"))
        db.set("user1", "name", "Grace")
        self.assertEqual(db.get("user1", "name"), "Grace")
        db.set("user2", "name", "Linus")
        self.assertEqual(db.get("user2", "name"), "Linus")

    def test_level_2_scan(self):
        db = InMemoryDB()
        for field, value in [("name", "Ada"), ("nickname", "ace"), ("city", "London")]:
            db.set("user1", field, value)
        self.assertEqual(db.scan("user1"), ["city(London)", "name(Ada)", "nickname(ace)"])
        self.assertEqual(db.scan_by_prefix("user1", "ni"), ["nickname(ace)"])
        self.assertEqual(db.scan_by_prefix("user1", "n"), ["name(Ada)", "nickname(ace)"])
        self.assertEqual(db.scan_by_prefix("user1", "missing"), [])
        self.assertEqual(db.scan("missing"), [])

    def test_level_3_ttl(self):
        db = InMemoryDB()
        db.set_at_with_ttl("a", "x", "1", 10, 5)
        db.set_at("a", "y", "2", 11)
        self.assertEqual(db.get_at("a", "x", 10), "1")
        self.assertEqual(db.get_at("a", "x", 14), "1")
        self.assertIsNone(db.get_at("a", "x", 15))
        self.assertFalse(db.delete_at("a", "x", 15))
        self.assertEqual(db.scan_at("a", 14), ["x(1)", "y(2)"])
        self.assertEqual(db.scan_at("a", 15), ["y(2)"])
        self.assertEqual(db.scan_by_prefix_at("a", "y", 99), ["y(2)"])
        db.set_at("a", "x", "permanent", 16)
        self.assertEqual(db.get_at("a", "x", 10_000), "permanent")
        self.assertTrue(db.delete_at("a", "x", 10_001))

    def test_level_4_backup_restore(self):
        db = InMemoryDB()
        db.set_at_with_ttl("a", "x", "1", 10, 10)
        db.set_at("b", "z", "9", 11)
        self.assertEqual(db.backup(15), 2)
        db.set_at("a", "x", "changed", 16)
        db.set_at("new", "field", "value", 17)
        db.restore(18, 15)
        self.assertEqual(db.get_at("a", "x", 19), "1")
        self.assertEqual(db.get_at("a", "x", 22), "1")
        self.assertIsNone(db.get_at("a", "x", 23))
        self.assertEqual(db.get_at("b", "z", 100), "9")
        self.assertIsNone(db.get_at("new", "field", 18))
        db.set_at("c", "v", "second", 25)
        self.assertEqual(db.backup(25), 2)
        db.restore(30, 24)
        self.assertIsNone(db.get_at("c", "v", 30))
        db.restore(30, 25)
        self.assertEqual(db.get_at("c", "v", 30), "second")


if __name__ == "__main__":
    unittest.main()
