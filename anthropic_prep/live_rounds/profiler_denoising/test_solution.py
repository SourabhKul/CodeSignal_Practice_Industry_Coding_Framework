import unittest
from solution import stacks_to_events


class TestProfilerDenoising(unittest.TestCase):
    def test_basic_events(self):
        samples = [
            (0, ["main"]),
            (1, ["main", "a"]),
            (3, ["main", "a", "b"]),
            (5, ["main", "a"]),
            (6, ["main"]),
            (7, []),
        ]
        self.assertEqual(stacks_to_events(samples), [
            {"name": "b", "start": 3, "end": 5},
            {"name": "a", "start": 1, "end": 6},
            {"name": "main", "start": 0, "end": 7},
        ])

    def test_recursion_and_min_duration(self):
        samples = [
            (0, ["f"]),
            (1, ["f", "f"]),
            (2, ["f"]),
            (5, []),
        ]
        self.assertEqual(stacks_to_events(samples, min_duration=2), [
            {"name": "f", "start": 0, "end": 5},
        ])


if __name__ == "__main__":
    unittest.main()

