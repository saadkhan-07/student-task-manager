"""Core logic for the Student Task Manager.

Keeps tasks in memory and saves them to a JSON file so they survive restarts.
"""
import json
import os
from dataclasses import dataclass, asdict


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False

    def __str__(self):
        mark = "x" if self.completed else " "
        return f"[{mark}] {self.id}. {self.title}"


class TaskManager:
    def __init__(self, storage_file=None):
        self.storage_file = storage_file
        self.tasks = []
        self.next_id = 1
        if storage_file:
            self.load()

    # ---------- add ----------
    def add_task(self, title):
        task = Task(id=self.next_id, title=title)
        self.tasks.append(task)
        self.next_id += 1
        self.save()
        return task

    # ---------- display ----------
    def list_tasks(self):
        return list(self.tasks)

    def find_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    # ---------- complete ----------
    def complete_task(self, task_id):
        raise NotImplementedError("Completing tasks is not implemented yet")

    # ---------- delete ----------
    def delete_task(self, task_id):
        task = self.find_task(task_id)
        if task is None:
            raise KeyError(f"No task with ID {task_id}")
        self.tasks.remove(task)
        self.save()
        return task

    # ---------- storage ----------
    def save(self):
        if not self.storage_file:
            return
        data = {"next_id": self.next_id, "tasks": [asdict(t) for t in self.tasks]}
        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def load(self):
        if not self.storage_file or not os.path.exists(self.storage_file):
            return
        with open(self.storage_file, encoding="utf-8") as f:
            data = json.load(f)
        self.tasks = [Task(**t) for t in data.get("tasks", [])]
        self.next_id = data.get("next_id", len(self.tasks) + 1)
