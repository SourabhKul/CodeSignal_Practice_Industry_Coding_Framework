import unittest
from solution import TimeVersionedKV


class TestTimeVersionedKV(unittest.TestCase):
    def test_level_1_basic_store(self):
        store = TimeVersionedKV()
        self.assertIsNone(store.set("mode", "fast"))
        self.assertEqual(store.get("mode"), "fast")
        self.assertTrue(store.delete("mode"))
        self.assertIsNone(store.get("mode"))
        self.assertFalse(store.delete("mode"))

    def test_level_2_prefix_queries(self):
        store = TimeVersionedKV()
        store.set("user:1", "Ada")
        store.set("user:2", "Grace")
        store.set("team:1", "Infra")
        self.assertEqual(store.keys("user:"), ["user:1", "user:2"])
        self.assertEqual(store.count("user:"), 2)
        self.assertEqual(store.keys("missing"), [])

    def test_level_3_time_versions(self):
        store = TimeVersionedKV()
        store.set_at(10, "a", "old")
        store.set_at(20, "a", "new")
        self.assertEqual(store.get_at(15, "a"), "old")
        self.assertEqual(store.get_at(20, "a"), "new")
        self.assertTrue(store.delete_at(30, "a"))
        self.assertIsNone(store.get_at(31, "a"))

    def test_level_4_compaction(self):
        store = TimeVersionedKV()
        store.set_at(10, "a", "old")
        store.set_at(20, "a", "new")
        self.assertEqual(store.compact(15), 0)
        self.assertEqual(store.compact(20), 1)
        self.assertEqual(store.get_at(20, "a"), "new")
        self.assertEqual(store.history("a"), ["20(new)"])


if __name__ == "__main__":
    unittest.main()

