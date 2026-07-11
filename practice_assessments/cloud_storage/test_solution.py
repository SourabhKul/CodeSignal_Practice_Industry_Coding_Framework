import importlib
import os
import unittest


CloudStorage = importlib.import_module(os.getenv("SOLUTION_MODULE", "solution")).CloudStorage


class TestCloudStorage(unittest.TestCase):
    def test_level_1_files(self):
        storage = CloudStorage()
        self.assertTrue(storage.add_file("/a.txt", 100))
        self.assertFalse(storage.add_file("/a.txt", 200))
        self.assertEqual(storage.get_file_size("/a.txt"), 100)
        self.assertIsNone(storage.get_file_size("/missing"))
        self.assertTrue(storage.copy_file("/a.txt", "/b.txt"))
        self.assertEqual(storage.get_file_size("/b.txt"), 100)
        self.assertFalse(storage.copy_file("/missing", "/c.txt"))
        self.assertFalse(storage.copy_file("/a.txt", "/b.txt"))

    def test_level_2_find_file(self):
        storage = CloudStorage()
        for name, size in [("/docs/a.txt", 100), ("/docs/b.txt", 200), ("/docs/c.log", 300), ("/docs/aa.txt", 200)]:
            storage.add_file(name, size)
        self.assertEqual(
            storage.find_file("/docs", ".txt"),
            ["/docs/aa.txt(200)", "/docs/b.txt(200)", "/docs/a.txt(100)"],
        )
        self.assertEqual(storage.find_file("/none", ".txt"), [])
        self.assertEqual(storage.find_file("/docs/a", ".txt"), ["/docs/aa.txt(200)", "/docs/a.txt(100)"])

    def test_level_3_users_capacity(self):
        storage = CloudStorage()
        self.assertTrue(storage.add_user("u1", 500))
        self.assertFalse(storage.add_user("u1", 1000))
        self.assertEqual(storage.add_file_by("u1", "/a.txt", 200), 300)
        self.assertIsNone(storage.add_file_by("u1", "/b.txt", 400))
        self.assertIsNone(storage.add_file_by("missing", "/x", 1))
        self.assertEqual(storage.copy_file_by("u1", "/a.txt", "/c.txt"), 100)
        self.assertIsNone(storage.copy_file_by("u1", "/a.txt", "/d.txt"))
        storage.add_file_by("u1", "/z.txt", 100)
        self.assertEqual(storage.update_capacity("u1", 300), 1)
        self.assertIsNone(storage.get_file_size("/c.txt"))
        self.assertEqual(storage.get_file_size("/a.txt"), 200)
        self.assertIsNone(storage.update_capacity("missing", 10))

    def test_level_4_backup_restore(self):
        storage = CloudStorage()
        storage.add_user("u1", 1000)
        storage.add_file_by("u1", "/a.txt", 100)
        storage.add_file_by("u1", "/b.txt", 200)
        self.assertEqual(storage.backup_user("u1"), 2)
        storage.add_file_by("u1", "/c.txt", 300)
        self.assertEqual(storage.restore_user("u1"), 2)
        self.assertEqual(storage.get_file_size("/a.txt"), 100)
        self.assertEqual(storage.get_file_size("/b.txt"), 200)
        self.assertIsNone(storage.get_file_size("/c.txt"))
        self.assertIsNone(storage.backup_user("missing"))
        storage.add_user("empty", 10)
        storage.add_file_by("empty", "/temporary", 1)
        self.assertEqual(storage.restore_user("empty"), 0)
        self.assertIsNone(storage.get_file_size("/temporary"))


if __name__ == "__main__":
    unittest.main()
