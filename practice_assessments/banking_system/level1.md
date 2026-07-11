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

### Examples

```python
bank = BankingSystem()
bank.create_account("a")      # True
bank.create_account("a")      # False
bank.deposit("a", 100)        # 100
bank.pay("a", 30)             # 70
bank.pay("a", 100)            # None
bank.deposit("missing", 10)   # None
```

