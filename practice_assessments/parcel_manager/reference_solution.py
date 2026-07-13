class ParcelManager:
    def __init__(self):
        self.parcels = {}
        self.couriers = set()
        self.history = [self._state_copy()]

    @staticmethod
    def _positive_integer(value):
        return isinstance(value, int) and not isinstance(value, bool) and value > 0

    @staticmethod
    def _identifier(value):
        return isinstance(value, str) and bool(value)

    def _state_copy(self):
        return {
            "parcels": {parcel_id: dict(parcel) for parcel_id, parcel in self.parcels.items()},
            "couriers": set(self.couriers),
        }

    def _record(self):
        self.history.append(self._state_copy())

    def add_parcel(self, parcel_id, size):
        if not self._identifier(parcel_id) or parcel_id in self.parcels or not self._positive_integer(size):
            return False
        self.parcels[parcel_id] = {"size": size, "status": "created", "courier": None}
        self._record()
        return True

    def get_parcel(self, parcel_id):
        parcel = self.parcels.get(parcel_id)
        if parcel is None:
            return None
        return {"size": parcel["size"], "status": parcel["status"]}

    def remove_parcel(self, parcel_id):
        if parcel_id not in self.parcels:
            return False
        del self.parcels[parcel_id]
        self._record()
        return True

    def find_parcels(self, prefix):
        if not isinstance(prefix, str):
            return []
        return sorted(parcel_id for parcel_id in self.parcels if parcel_id.startswith(prefix))

    def top_parcels(self, count):
        if not self._positive_integer(count):
            return []
        parcels = sorted(self.parcels.items(), key=lambda item: (-item[1]["size"], item[0]))
        return [(parcel_id, parcel["size"]) for parcel_id, parcel in parcels[:count]]

    def add_courier(self, courier_id):
        if not self._identifier(courier_id) or courier_id in self.couriers:
            return False
        self.couriers.add(courier_id)
        self._record()
        return True

    def assign_courier(self, parcel_id, courier_id):
        parcel = self.parcels.get(parcel_id)
        if parcel is None or courier_id not in self.couriers or parcel["courier"] == courier_id:
            return False
        parcel["courier"] = courier_id
        self._record()
        return True

    def assigned_courier(self, parcel_id):
        parcel = self.parcels.get(parcel_id)
        return None if parcel is None else parcel["courier"]

    def update_status(self, parcel_id, status):
        parcel = self.parcels.get(parcel_id)
        if (
            parcel is None
            or parcel["courier"] is None
            or not isinstance(status, str)
            or not status
            or status == parcel["status"]
        ):
            return False
        parcel["status"] = status
        self._record()
        return True

    def rollback(self, version):
        if (
            not isinstance(version, int)
            or isinstance(version, bool)
            or version < 0
            or version >= len(self.history)
        ):
            return False
        state = self.history[version]
        self.parcels = {parcel_id: dict(parcel) for parcel_id, parcel in state["parcels"].items()}
        self.couriers = set(state["couriers"])
        self.history = self.history[: version + 1]
        return True
