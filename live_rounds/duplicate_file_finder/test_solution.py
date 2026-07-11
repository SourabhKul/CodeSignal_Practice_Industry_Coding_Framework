import os
import tempfile
import unittest
from solution import find_duplicate_files


class TestDuplicateFileFinder(unittest.TestCase):
    def test_duplicate_groups(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = {
                "a.txt": b"same",
                "nested/b.txt": b"same",
                "c.txt": b"other",
                "d.txt": b"other",
                "e.txt": b"unique",
            }
            for name, content in paths.items():
                path = os.path.join(tmp, name)
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "wb") as f:
                    f.write(content)
            groups = find_duplicate_files(tmp)
            rel_groups = [[os.path.relpath(path, tmp) for path in group] for group in groups]
            self.assertEqual(rel_groups, [["a.txt", "nested/b.txt"], ["c.txt", "d.txt"]])


if __name__ == "__main__":
    unittest.main()

