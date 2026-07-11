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

## Level 4 - Extending Design & Functionality

- **merge_accounts_at(timestamp, account_id_1, account_id_2)**
  - Merge `account_id_2` into `account_id_1`.
  - Return `True` if the accounts were merged, otherwise return `False`.
  - If either account does not exist, return `False`.
  - If the accounts are the same, return `False`.
  - The balance and outgoing total of `account_id_2` are added to `account_id_1`.
  - After merging, `account_id_2` should no longer exist.
  - Pending incoming transfers targeting `account_id_2` should now target `account_id_1`.
  - Pending outgoing transfers from `account_id_2` should now originate from `account_id_1`.
- **get_balance_at(timestamp, account_id, query_timestamp)**
  - Return the balance of `account_id` at `query_timestamp`, or `None` if the account did not exist at that time.
  - If an account was merged into another account, historical queries for the old account id before the merge should still work.
  - Historical queries after the merge for the old account id should return `None`.

### Examples

```python
bank = BankingSystem()
bank.create_account_at(1, "a")             # True
bank.create_account_at(2, "b")             # True
bank.deposit_at(3, "a", 100)               # 100
bank.deposit_at(4, "b", 50)                # 50
bank.merge_accounts_at(5, "a", "b")        # True
bank.deposit_at(6, "a", 0)                 # 150
bank.deposit_at(7, "b", 0)                 # None
bank.get_balance_at(8, "a", 4)             # 100
bank.get_balance_at(8, "a", 6)             # 150
bank.get_balance_at(8, "b", 4)             # 50
bank.get_balance_at(8, "b", 6)             # None
```
