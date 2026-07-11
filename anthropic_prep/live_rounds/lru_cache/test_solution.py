import os
import tempfile
import unittest
from solution import PersistentLRUCache


class TestPersistentLRUCache(unittest.TestCase):
    def test_lru_eviction(self):
        with tempfile.TemporaryDirectory() as tmp:
            cache = PersistentLRUCache(2, os.path.join(tmp, "cache.json"))
            cache.put("a", 1)
            cache.put("b", 2)
            self.assertEqual(cache.get("a"), 1)
            cache.put("c", 3)
            self.assertIsNone(cache.get("b"))
            self.assertEqual(cache.get("a"), 1)
            self.assertEqual(cache.get("c"), 3)

    def test_persistence(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "cache.json")
            cache = PersistentLRUCache(2, path)
            cache.put("a", {"x": 1})
            cache.put("b", [1, 2])
            cache.save()
            restored = PersistentLRUCache(2, path)
            restored.load()
            self.assertEqual(restored.get("a"), {"x": 1})
            self.assertEqual(restored.get("b"), [1, 2])


if __name__ == "__main__":
    unittest.main()

