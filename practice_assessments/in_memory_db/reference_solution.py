from copy import deepcopy


class InMemoryDB:
    def __init__(self):
        self.records = {}
        self.backups = {}

    def set(self, key, field, value):
        self.records.setdefault(key, {})[field] = (value, None)

    def get(self, key, field):
        entry = self.records.get(key, {}).get(field)
        return None if entry is None else entry[0]

    def delete(self, key, field):
        fields = self.records.get(key)
        if fields is None or field not in fields:
            return False
        del fields[field]
        if not fields:
            del self.records[key]
        return True

    def scan(self, key):
        return [f"{field}({value})" for field, (value, _) in sorted(self.records.get(key, {}).items())]

    def scan_by_prefix(self, key, prefix):
        return [
            f"{field}({value})"
            for field, (value, _) in sorted(self.records.get(key, {}).items())
            if field.startswith(prefix)
        ]

    def set_at(self, key, field, value, timestamp):
        self.records.setdefault(key, {})[field] = (str(value), None)

    def set_at_with_ttl(self, key, field, value, timestamp, ttl):
        self.records.setdefault(key, {})[field] = (str(value), timestamp + ttl)

    def _live_entry(self, key, field, timestamp):
        entry = self.records.get(key, {}).get(field)
        if entry is None:
            return None
        value, expires_at = entry
        return entry if expires_at is None or timestamp < expires_at else None

    def get_at(self, key, field, timestamp):
        entry = self._live_entry(key, field, timestamp)
        return None if entry is None else entry[0]

    def delete_at(self, key, field, timestamp):
        if self._live_entry(key, field, timestamp) is None:
            return False
        return self.delete(key, field)

    def scan_at(self, key, timestamp):
        return [
            f"{field}({entry[0]})"
            for field in sorted(self.records.get(key, {}))
            if (entry := self._live_entry(key, field, timestamp)) is not None
        ]

    def scan_by_prefix_at(self, key, prefix, timestamp):
        return [
            f"{field}({entry[0]})"
            for field in sorted(self.records.get(key, {}))
            if field.startswith(prefix)
            and (entry := self._live_entry(key, field, timestamp)) is not None
        ]

    def backup(self, timestamp):
        snapshot = {}
        for key, fields in self.records.items():
            live_fields = {}
            for field, (value, expires_at) in fields.items():
                if expires_at is not None and timestamp >= expires_at:
                    continue
                remaining_ttl = None if expires_at is None else expires_at - timestamp
                live_fields[field] = (value, remaining_ttl)
            if live_fields:
                snapshot[key] = live_fields
        self.backups[timestamp] = deepcopy(snapshot)
        return len(snapshot)

    def restore(self, timestamp, restore_to):
        candidates = [backup_time for backup_time in self.backups if backup_time <= restore_to]
        if not candidates:
            return None
        snapshot = self.backups[max(candidates)]
        self.records = {
            key: {
                field: (value, None if remaining_ttl is None else timestamp + remaining_ttl)
                for field, (value, remaining_ttl) in fields.items()
            }
            for key, fields in deepcopy(snapshot).items()
        }
        return None
