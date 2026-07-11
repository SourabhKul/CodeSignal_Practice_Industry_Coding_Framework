import importlib
import os
import unittest


TaskManager = importlib.import_module(os.getenv("SOLUTION_MODULE", "solution")).TaskManager


class TestTaskManager(unittest.TestCase):
    def test_level_1_crud(self):
        manager = TaskManager()
        self.assertTrue(manager.add_task("t1", 10))
        self.assertFalse(manager.add_task("t1", 20))
        self.assertEqual(manager.get_task("t1"), {"priority": 10, "status": "open"})
        self.assertTrue(manager.update_task("t1", 30))
        self.assertEqual(manager.get_task("t1"), {"priority": 30, "status": "open"})
        self.assertFalse(manager.update_task("missing", 1))
        self.assertIsNone(manager.get_task("missing"))

    def test_level_2_search(self):
        manager = TaskManager()
        manager.add_task("old-high", 20)
        manager.add_task("low", 5)
        manager.add_task("new-high", 20)
        manager.add_task("middle", 10)
        self.assertEqual(manager.search_tasks(10, 20), ["new-high", "old-high", "middle"])
        self.assertEqual(manager.search_tasks(20, 20), ["new-high", "old-high"])
        self.assertEqual(manager.search_tasks(100, 200), [])
        manager.update_task("low", 30)
        self.assertEqual(manager.search_tasks(0, 100)[0], "low")

    def test_level_3_quota_ttl(self):
        manager = TaskManager()
        for task_id in ["a", "b", "c"]:
            manager.add_task(task_id, 10)
        self.assertTrue(manager.add_user("u", 1))
        self.assertFalse(manager.add_user("u", 2))
        self.assertFalse(manager.assign_task_at(1, "a", "missing", 5))
        self.assertTrue(manager.assign_task_at(1, "a", "u", 5))
        self.assertFalse(manager.assign_task_at(2, "b", "u", 5))
        self.assertEqual(manager.active_tasks_at(5, "u"), ["a"])
        self.assertEqual(manager.active_tasks_at(6, "u"), [])
        self.assertTrue(manager.assign_task_at(6, "b", "u", 5))
        self.assertEqual(manager.active_tasks_at(7, "u"), ["b"])
        self.assertIsNone(manager.active_tasks_at(7, "missing"))

    def test_level_4_lifecycle(self):
        manager = TaskManager()
        for task_id in ["a", "b", "c"]:
            manager.add_task(task_id, 10)
        manager.add_user("u", 2)
        manager.assign_task_at(1, "a", "u", 5)
        manager.assign_task_at(2, "b", "u", 10)
        self.assertTrue(manager.complete_task_at(5, "a"))
        self.assertFalse(manager.complete_task_at(6, "a"))
        self.assertFalse(manager.complete_task_at(6, "c"))
        self.assertEqual(manager.overdue_tasks(11), [])
        self.assertEqual(manager.overdue_tasks(12), ["b"])
        self.assertEqual(manager.get_task("a"), {"priority": 10, "status": "completed"})
        self.assertEqual(manager.get_task("b"), {"priority": 10, "status": "expired"})


if __name__ == "__main__":
    unittest.main()
