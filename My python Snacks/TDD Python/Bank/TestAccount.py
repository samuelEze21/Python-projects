import unittest
from SamuelPythonProjects.Bank.account import Account


class MyTestCase(unittest.TestCase):

    def test_that_New_account_balance_is_Zero(self):
        account = Account("David", "1111", 0.00, "22222")
        self.assertTrue(account.get_account_balance)


    def test_that_When_New_account_deposit_2k_balance_is_2k(self):
        account = Account("David", "1111", 0.00, "22222")
        account.deposit_amount(2000)
        self.assertEqual(account.get_account_balance("1111"), 2000)


    def test_that_When_New_account_Deposit_2k_And_withdraw_5k_balance_is_2k(self):
        account = Account("DAvid", "1111", 1000, "22222")
        account.deposit_amount(2000)
        self.assertEqual(account.get_account_balance("1111"), 3000)


    def test_that_When_New_account_deposit_2k_withdraw_1k_balance_is_1k(self):
       account = Account("DAvid", "1111", 1000, "22222")
       account.deposit_amount(2000)
       self.assertEqual(account.get_account_balance("1111"), 3000)
       account.withdraw("1111", 1000)
       self.assertEqual(account.get_account_balance("1111"), 2000)









