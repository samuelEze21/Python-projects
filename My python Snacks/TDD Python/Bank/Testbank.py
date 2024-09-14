import unittest
from SamuelPythonProjects.Bank.bank import Bank



class BankTestCase(unittest.TestCase):

    def setUp(self):
        Bank.total_Number_Of_Account = 0

    def test_that_when_a_user_creates_Account_total_account_created_is_One(self):
        self.bank = Bank()
        account = self.bank.create_new_account("David", "1111", 500.00)
        self.assertEqual(self.bank.total_Number_Of_Account, 1)
        self.assertEqual(account.name, "David")
        self.assertEqual(account.balance, 500.00)
        self.assertEqual(account.pin, "1111")


    def testThatWhen_Two_Users_CreateAccount_TotalNumberOfAccountEquals_Two(self):
        self.bank = Bank()
        account1 = self.bank.create_new_account("David", "1111", 500.00)
        account2 = self.bank.create_new_account("Sam", "2222", 400.00)
        self.assertEqual(self.bank.total_Number_Of_Account, 2)
        self.assertEqual(account1.name, "David")
        self.assertEqual(account1.balance, 500.00)
        self.assertEqual(account1.pin, "1111")
        self.assertEqual(account2.name, "Sam")
        self.assertEqual(account2.balance, 400.00)
        self.assertEqual(account2.pin, "2222")


    def testThat_when2kIsDeposited_ToAccount1_BalanceIs2k(self):
        self.bank = Bank()
        account = self.bank.create_new_account("David", "1111", 0.00)
        new_balance = self.bank.deposit_to_account(2000, account.account_number)
        self.assertEqual(2000.00, new_balance)



    def testThat_when2kIsDeposited_ToAccount1_And_withdraw_1k_BalanceIs1k(self):
        self.bank = Bank()
        account = self.bank.create_new_account("David", "1111", 0.00)
        new_balance = self.bank.deposit_to_account(2000, account.account_number)
        self.assertEqual(2000.00, new_balance)
        new_balance = self.bank.withdraw_from_account(1000,  account.account_number, "1111")
        self.assertEqual(1000.00, new_balance)



if __name__ == '__main__':
    unittest.main()
