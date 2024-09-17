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


    def testThat_when2k_isDeposited_ToAccount1_BalanceIs2k_AND_act1_can_Transfer_1k_to_account2(self):
        self.bank = Bank()
        account_1 = self.bank.create_new_account(" Basil peters", "7788", 0.00)
        new_balance = self.bank.deposit_to_account(2000, account_1.account_number)
        self.assertEqual(2000.00, new_balance)
        account_2 = self.bank.create_new_account(" John King", "5566", 0.00)
        new_balance_account_1_balance_account_2_balance  = self.bank.transfer(account_1.account_number, 1000, account_2.account_number, 1000)




if __name__ == '__main__':
    unittest.main()
