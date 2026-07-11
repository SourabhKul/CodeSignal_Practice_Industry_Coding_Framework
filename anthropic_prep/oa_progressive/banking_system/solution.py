class BankingSystem:
    """Candidate workspace. Add later-level methods only after unlocking them."""

    def __init__(self):
        self.accounts = {} # {account_id : {'balance': balance, 'outgoing': outgoing}}

    def create_account(self, account_id):
        if account_id in self.accounts.keys():
            return False
        self.accounts[account_id] = {
            'balance': 0,
            'outgoing': 0
        }
        return True

    def deposit(self, account_id, amount):
        if account_id not in self.accounts.keys():
            return None
        self.accounts[account_id]['balance'] += amount
        return self.accounts[account_id]['balance']

    def pay(self, account_id, amount):
        if account_id not in self.accounts.keys():
            return None
        elif self.accounts[account_id]['balance'] < amount:
            return None
        else:
            self.accounts[account_id]['balance'] -= amount
            self.accounts[account_id]['outgoing'] += amount
        return self.accounts[account_id]['balance']
    
    def top_spenders(self, n):
            sorted_accounts = sorted(self.accounts, key=lambda account_id: (-self.accounts[account_id]['outgoing'], account_id))
            to_return = []
            if len(sorted_accounts) < n:
                for account_id in sorted_accounts:
                    to_return.append(f"{account_id}({self.accounts[account_id]['outgoing']})")
                return to_return
            else:
                for account_id in sorted_accounts[:n]:
                    to_return.append(f"{account_id}({self.accounts[account_id]['outgoing']})")
                return to_return


