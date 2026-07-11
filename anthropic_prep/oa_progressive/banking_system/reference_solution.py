class BankingSystem:
    TRANSFER_TTL_MS = 86_400_000

    def __init__(self):
        self.accounts = {}
        self.transfers = {}
        self.transfer_sequence = 0
        self.history = {}

    def _record(self, timestamp, account_id):
        balance = self.accounts.get(account_id, {}).get("balance")
        self.history.setdefault(account_id, []).append((timestamp, balance))

    def _expire_transfers(self, timestamp):
        for transfer in self.transfers.values():
            if transfer["status"] != "pending" or timestamp < transfer["expires_at"]:
                continue
            transfer["status"] = "expired"
            source = transfer["source"]
            if source in self.accounts:
                self.accounts[source]["balance"] += transfer["amount"]
                self._record(timestamp, source)

    def create_account(self, account_id):
        return self.create_account_at(0, account_id)

    def deposit(self, account_id, amount):
        return self.deposit_at(0, account_id, amount)

    def pay(self, account_id, amount):
        return self.pay_at(0, account_id, amount)

    def top_spenders(self, n):
        return self.top_spenders_at(0, n)

    def create_account_at(self, timestamp, account_id):
        self._expire_transfers(timestamp)
        if account_id in self.accounts:
            return False
        self.accounts[account_id] = {"balance": 0, "outgoing": 0}
        self._record(timestamp, account_id)
        return True

    def deposit_at(self, timestamp, account_id, amount):
        self._expire_transfers(timestamp)
        if account_id not in self.accounts:
            return None
        self.accounts[account_id]["balance"] += amount
        self._record(timestamp, account_id)
        return self.accounts[account_id]["balance"]

    def pay_at(self, timestamp, account_id, amount):
        self._expire_transfers(timestamp)
        account = self.accounts.get(account_id)
        if account is None or account["balance"] < amount:
            return None
        account["balance"] -= amount
        account["outgoing"] += amount
        self._record(timestamp, account_id)
        return account["balance"]

    def top_spenders_at(self, timestamp, n):
        self._expire_transfers(timestamp)
        ranked = sorted(self.accounts.items(), key=lambda item: (-item[1]["outgoing"], item[0]))
        return [f"{account_id}({account['outgoing']})" for account_id, account in ranked[:n]]

    def transfer_at(self, timestamp, source_account_id, target_account_id, amount):
        self._expire_transfers(timestamp)
        source = self.accounts.get(source_account_id)
        if (
            source is None
            or target_account_id not in self.accounts
            or source_account_id == target_account_id
            or source["balance"] < amount
        ):
            return None
        source["balance"] -= amount
        self._record(timestamp, source_account_id)
        self.transfer_sequence += 1
        transfer_id = f"transfer{self.transfer_sequence}"
        self.transfers[transfer_id] = {
            "source": source_account_id,
            "target": target_account_id,
            "amount": amount,
            "expires_at": timestamp + self.TRANSFER_TTL_MS,
            "status": "pending",
        }
        return transfer_id

    def accept_transfer_at(self, timestamp, account_id, transfer_id):
        self._expire_transfers(timestamp)
        transfer = self.transfers.get(transfer_id)
        if transfer is None or transfer["status"] != "pending" or transfer["target"] != account_id:
            return False
        source = transfer["source"]
        if source not in self.accounts or account_id not in self.accounts:
            return False
        transfer["status"] = "accepted"
        self.accounts[account_id]["balance"] += transfer["amount"]
        self.accounts[source]["outgoing"] += transfer["amount"]
        self._record(timestamp, account_id)
        return True

    def merge_accounts_at(self, timestamp, account_id_1, account_id_2):
        self._expire_transfers(timestamp)
        if account_id_1 == account_id_2 or account_id_1 not in self.accounts or account_id_2 not in self.accounts:
            return False
        first = self.accounts[account_id_1]
        second = self.accounts[account_id_2]
        first["balance"] += second["balance"]
        first["outgoing"] += second["outgoing"]
        del self.accounts[account_id_2]
        self._record(timestamp, account_id_1)
        self._record(timestamp, account_id_2)
        for transfer in self.transfers.values():
            if transfer["status"] != "pending":
                continue
            if transfer["source"] == account_id_2:
                transfer["source"] = account_id_1
            if transfer["target"] == account_id_2:
                transfer["target"] = account_id_1
        return True

    def get_balance_at(self, timestamp, account_id, query_timestamp):
        self._expire_transfers(timestamp)
        result = None
        seen = False
        for event_timestamp, balance in self.history.get(account_id, []):
            if event_timestamp <= query_timestamp:
                result = balance
                seen = True
        return result if seen else None
