# Scenario

Your task is to implement a simplified version of a banking system.
All operations that should be supported are listed below. Partial credit will be granted for each test passed, so
run tests often and receive partial credit for passed tests. Please check tests for requirements and argument types.

### Implementation Tips

Read the question all the way through before you start coding, but implement the operations and complete the
levels one by one, not all together, keeping in mind that you will need to refactor to support additional functionality.
Please, do not change the existing method signatures.

## Task

The banking system stores accounts, balances, outgoing payments, and later timestamped transfers and history.

Example of account state:

```plaintext
[bank]
    +- acct-a
    |   Balance: 700
    |   Outgoing: 300
    +- acct-b
    |   Balance: 300
    |   Outgoing: 0
```

## Level 1 - Initial Design & Basic Functions

- **create_account(account_id)**
  - Create a new account with balance `0`.
  - If an account with the same id already exists, return `False`.
  - Otherwise, return `True`.
- **deposit(account_id, amount)**
  - Deposit `amount` into the account.
  - Return the new balance.
  - If the account does not exist, return `None`.
- **pay(account_id, amount)**
  - Withdraw `amount` from the account.
  - Return the new balance.
  - If the account does not exist, return `None`.
  - If the account has insufficient funds, return `None`.
  - Successful payments count as outgoing money for that account.

## Level 2 - Data Structures & Data Processing

- **top_spenders(n)**
  - Return the top `n` accounts ordered by total outgoing money in descending order.
  - In case of a tie, order by account id in ascending lexicographical order.
  - Return values in the format `["account_id(total_outgoing)", ...]`.
  - Accounts with `0` outgoing money should be included if needed to return up to `n` accounts.
  - If there are fewer than `n` accounts, return all accounts.

### Examples

```python
bank = BankingSystem()
bank.create_account("b")      # True
bank.create_account("a")      # True
bank.create_account("c")      # True
bank.deposit("a", 1000)       # 1000
bank.deposit("b", 1000)       # 1000
bank.deposit("c", 1000)       # 1000
bank.pay("b", 200)            # 800
bank.pay("a", 200)            # 800
bank.pay("c", 100)            # 900
bank.top_spenders(3)          # ["a(200)", "b(200)", "c(100)"]

bank.create_account("d")      # True
bank.top_spenders(4)          # ["a(200)", "b(200)", "c(100)", "d(0)"]
```

