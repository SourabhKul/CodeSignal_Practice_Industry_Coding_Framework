from copy import deepcopy


class CloudStorage:
    def __init__(self):
        self.files = {}
        self.users = {}
        self.backups = {}

    def add_file(self, name, size):
        if name in self.files:
            return False
        self.files[name] = {"size": size, "owner": None}
        return True

    def copy_file(self, source, dest):
        file = self.files.get(source)
        if file is None or dest in self.files:
            return False
        owner = file["owner"]
        if owner is not None and self._remaining(owner) < file["size"]:
            return False
        self.files[dest] = deepcopy(file)
        return True

    def get_file_size(self, name):
        file = self.files.get(name)
        return None if file is None else file["size"]

    def find_file(self, prefix, suffix):
        matches = [
            (name, file["size"])
            for name, file in self.files.items()
            if name.startswith(prefix) and name.endswith(suffix)
        ]
        matches.sort(key=lambda item: (-item[1], item[0]))
        return [f"{name}({size})" for name, size in matches]

    def add_user(self, user_id, capacity):
        if user_id in self.users:
            return False
        self.users[user_id] = capacity
        return True

    def _usage(self, user_id):
        return sum(file["size"] for file in self.files.values() if file["owner"] == user_id)

    def _remaining(self, user_id):
        return self.users[user_id] - self._usage(user_id)

    def add_file_by(self, user_id, name, size):
        if user_id not in self.users or name in self.files or self._remaining(user_id) < size:
            return None
        self.files[name] = {"size": size, "owner": user_id}
        return self._remaining(user_id)

    def copy_file_by(self, user_id, source, dest):
        file = self.files.get(source)
        if (
            user_id not in self.users
            or file is None
            or file["owner"] != user_id
            or dest in self.files
            or self._remaining(user_id) < file["size"]
        ):
            return None
        self.files[dest] = deepcopy(file)
        return self._remaining(user_id)

    def update_capacity(self, user_id, capacity):
        if user_id not in self.users:
            return None
        self.users[user_id] = capacity
        owned = [
            (file["size"], name)
            for name, file in self.files.items()
            if file["owner"] == user_id
        ]
        owned.sort(reverse=True)
        removed = 0
        for _, name in owned:
            if self._usage(user_id) <= capacity:
                break
            del self.files[name]
            removed += 1
        return removed

    def backup_user(self, user_id):
        if user_id not in self.users:
            return None
        snapshot = {
            name: file["size"]
            for name, file in self.files.items()
            if file["owner"] == user_id
        }
        self.backups[user_id] = snapshot
        return len(snapshot)

    def restore_user(self, user_id):
        if user_id not in self.users:
            return None
        for name in [name for name, file in self.files.items() if file["owner"] == user_id]:
            del self.files[name]
        restored = 0
        for name, size in self.backups.get(user_id, {}).items():
            if name in self.files:
                continue
            self.files[name] = {"size": size, "owner": user_id}
            restored += 1
        return restored
