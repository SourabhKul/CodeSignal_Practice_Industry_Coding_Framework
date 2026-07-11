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

## Level 3 - Refactoring & Encapsulation

Operations can now be performed at specific timestamps, and money can be transferred between accounts.
Implement extensions of existing methods which inherit all functionality but also include a timestamp for the operation.

- **create_account_at(timestamp, account_id)**
- **deposit_at(timestamp, account_id, amount)**
- **pay_at(timestamp, account_id, amount)**
- **top_spenders_at(timestamp, n)**
  - These timestamped methods have the same behavior as their non-timestamped equivalents.
- **transfer_at(timestamp, source_account_id, target_account_id, amount)**
  - Create a pending transfer from `source_account_id` to `target_account_id`.
  - Return a unique transfer id in the format `"transfer1"`, `"transfer2"`, etc.
  - If either account does not exist, return `None`.
  - If source and target are the same account, return `None`.
  - If the source account has insufficient funds, return `None`.
  - The transfer amount is withheld from the source account immediately.
  - Pending transfers expire after `86400000` milliseconds (24 hours).
- **accept_transfer_at(timestamp, account_id, transfer_id)**
  - Accept the pending transfer for `account_id`.
  - Return `True` if the transfer was accepted, otherwise return `False`.
  - The accepting account must be the target account.
  - Expired transfers cannot be accepted, and their withheld amount should be returned to the source account.
  - Accepted transfers add the amount to the target account.
  - Accepted transfers count as outgoing money for the source account.

### Examples

```python
bank = BankingSystem()
bank.create_account_at(1, "a")                 # True
bank.create_account_at(2, "b")                 # True
bank.deposit_at(3, "a", 500)                   # 500
tid = bank.transfer_at(4, "a", "b", 300)       # "transfer1"
bank.deposit_at(5, "a", 0)                     # 200
bank.accept_transfer_at(6, "b", tid)           # True
bank.deposit_at(7, "b", 0)                     # 300
bank.top_spenders_at(8, 2)                     # ["a(300)", "b(0)"]

expired = bank.transfer_at(10, "a", "b", 100)  # "transfer2"
bank.accept_transfer_at(10 + 86400000, "b", expired)
# False
```
