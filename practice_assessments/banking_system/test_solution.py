import importlib
import os
import unittest


BankingSystem = importlib.import_module(os.getenv("SOLUTION_MODULE", "solution")).BankingSystem


class TestBankingSystem(unittest.TestCase):
    def test_level_1_accounts(self):
        bank = BankingSystem()
        self.assertTrue(bank.create_account("a"))
        self.assertFalse(bank.create_account("a"))
        self.assertEqual(bank.deposit("a", 100), 100)
        self.assertEqual(bank.deposit("a", 25), 125)
        self.assertEqual(bank.pay("a", 30), 95)
        self.assertIsNone(bank.deposit("missing", 10))
        self.assertIsNone(bank.pay("missing", 10))
        self.assertIsNone(bank.pay("a", 1000))
        self.assertEqual(bank.deposit("a", 0), 95)

    def test_level_2_top_spenders(self):
        bank = BankingSystem()
        for account_id in ["b", "a", "c", "d"]:
            bank.create_account(account_id)
            bank.deposit(account_id, 1000)
        bank.pay("b", 200)
        bank.pay("a", 200)
        bank.pay("c", 100)
        self.assertEqual(bank.top_spenders(2), ["a(200)", "b(200)"])
        self.assertEqual(bank.top_spenders(4), ["a(200)", "b(200)", "c(100)", "d(0)"])
        self.assertEqual(bank.top_spenders(10), ["a(200)", "b(200)", "c(100)", "d(0)"])

    def test_level_3_transfers(self):
        bank = BankingSystem()
        bank.create_account_at(1, "a")
        bank.create_account_at(2, "b")
        bank.deposit_at(3, "a", 500)
        self.assertIsNone(bank.transfer_at(4, "a", "a", 1))
        self.assertIsNone(bank.transfer_at(4, "missing", "b", 1))
        self.assertIsNone(bank.transfer_at(4, "a", "b", 1000))
        transfer_id = bank.transfer_at(5, "a", "b", 300)
        self.assertEqual(transfer_id, "transfer1")
        self.assertEqual(bank.deposit_at(6, "a", 0), 200)
        self.assertFalse(bank.accept_transfer_at(7, "a", transfer_id))
        self.assertTrue(bank.accept_transfer_at(8, "b", transfer_id))
        self.assertFalse(bank.accept_transfer_at(9, "b", transfer_id))
        self.assertEqual(bank.deposit_at(10, "b", 0), 300)
        self.assertEqual(bank.top_spenders_at(11, 2), ["a(300)", "b(0)"])
        expired = bank.transfer_at(20, "a", "b", 100)
        self.assertFalse(bank.accept_transfer_at(20 + 86_400_000, "b", expired))
        self.assertEqual(bank.deposit_at(20 + 86_400_001, "a", 0), 200)

    def test_level_4_merge_history(self):
        bank = BankingSystem()
        bank.create_account_at(1, "a")
        bank.create_account_at(2, "b")
        bank.deposit_at(3, "a", 100)
        bank.deposit_at(4, "b", 50)
        self.assertFalse(bank.merge_accounts_at(5, "a", "a"))
        self.assertFalse(bank.merge_accounts_at(5, "a", "missing"))
        self.assertTrue(bank.merge_accounts_at(5, "a", "b"))
        self.assertEqual(bank.deposit_at(6, "a", 0), 150)
        self.assertIsNone(bank.deposit_at(7, "b", 0))
        self.assertEqual(bank.get_balance_at(8, "a", 2), 0)
        self.assertEqual(bank.get_balance_at(8, "a", 4), 100)
        self.assertEqual(bank.get_balance_at(8, "a", 6), 150)
        self.assertEqual(bank.get_balance_at(8, "b", 4), 50)
        self.assertIsNone(bank.get_balance_at(8, "b", 6))
        self.assertIsNone(bank.get_balance_at(8, "missing", 6))


if __name__ == "__main__":
    unittest.main()
