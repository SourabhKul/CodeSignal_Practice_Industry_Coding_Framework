class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.users = {}
        self.creation_sequence = 0

    def add_task(self, task_id, priority):
        if task_id in self.tasks:
            return False
        self.creation_sequence += 1
        self.tasks[task_id] = {
            "priority": priority,
            "status": "open",
            "created": self.creation_sequence,
            "user": None,
            "expires_at": None,
        }
        return True

    def update_task(self, task_id, new_priority):
        task = self.tasks.get(task_id)
        if task is None or task["status"] != "open":
            return False
        task["priority"] = new_priority
        return True

    def get_task(self, task_id):
        task = self.tasks.get(task_id)
        if task is None:
            return None
        return {"priority": task["priority"], "status": task["status"]}

    def search_tasks(self, min_priority, max_priority):
        matches = [
            (task_id, task)
            for task_id, task in self.tasks.items()
            if task["status"] == "open" and min_priority <= task["priority"] <= max_priority
        ]
        matches.sort(key=lambda item: (-item[1]["priority"], -item[1]["created"]))
        return [task_id for task_id, _ in matches]

    def add_user(self, user_id, quota):
        if user_id in self.users:
            return False
        self.users[user_id] = quota
        return True

    def _expire(self, timestamp):
        for task in self.tasks.values():
            if task["status"] == "open" and task["user"] is not None and timestamp >= task["expires_at"]:
                task["status"] = "expired"

    def _active_count(self, user_id):
        return sum(
            task["status"] == "open" and task["user"] == user_id
            for task in self.tasks.values()
        )

    def assign_task_at(self, timestamp, task_id, user_id, ttl):
        self._expire(timestamp)
        task = self.tasks.get(task_id)
        if (
            user_id not in self.users
            or task is None
            or task["status"] != "open"
            or task["user"] is not None
            or self._active_count(user_id) >= self.users[user_id]
        ):
            return False
        task["user"] = user_id
        task["expires_at"] = timestamp + ttl
        return True

    def active_tasks_at(self, timestamp, user_id):
        self._expire(timestamp)
        if user_id not in self.users:
            return None
        return sorted(
            task_id
            for task_id, task in self.tasks.items()
            if task["status"] == "open" and task["user"] == user_id
        )

    def complete_task_at(self, timestamp, task_id):
        self._expire(timestamp)
        task = self.tasks.get(task_id)
        if task is None or task["status"] != "open" or task["user"] is None:
            return False
        task["status"] = "completed"
        return True

    def overdue_tasks(self, timestamp):
        self._expire(timestamp)
        return sorted(task_id for task_id, task in self.tasks.items() if task["status"] == "expired")
