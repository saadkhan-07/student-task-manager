import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from task_manager import TaskManager  # noqa: E402


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Finish DevOps assignment")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Finish DevOps assignment")
        self.assertFalse(task.completed)
        self.assertEqual(len(self.manager.list_tasks()), 1)

    def test_add_task_rejects_empty_title(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")
        self.assertEqual(self.manager.list_tasks(), [])

    def test_complete_task(self):
        task = self.manager.add_task("Read chapter 4")
        self.manager.complete_task(task.id)
        self.assertTrue(self.manager.find_task(task.id).completed)

    def test_complete_unknown_task_raises(self):
        with self.assertRaises(KeyError):
            self.manager.complete_task(99)

    def test_delete_task(self):
        first = self.manager.add_task("Task one")
        second = self.manager.add_task("Task two")
        self.manager.delete_task(first.id)
        remaining = self.manager.list_tasks()
        self.assertEqual(len(remaining), 2)
        self.assertEqual(remaining[0].id, second.id)

    def test_tasks_are_saved_to_file(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "tasks.json")
            TaskManager(path).add_task("Persisted task")
            reloaded = TaskManager(path)
            self.assertEqual(reloaded.list_tasks()[0].title, "Persisted task")


if __name__ == "__main__":
    unittest.main()
