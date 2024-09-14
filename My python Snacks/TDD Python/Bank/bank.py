from SamuelPythonProjects.Bank.account import Account


class Bank:
    total_Number_Of_Account = 0

    def __init__(self):
        self.accounts = []


    def create_new_account(self, name, pin, balance):
        Bank.total_Number_Of_Account += 1
        account_number = self.account_number_generator()
        new_account = Account(name, pin, balance, account_number)
        self.accounts.append(new_account)
        return new_account


    @staticmethod
    def account_number_generator():
        return "222333" + str(Bank.total_Number_Of_Account)

    def account_number_validator(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None


    def deposit_to_account(self, amount, account_number):
        account = self.account_number_validator(account_number)
        if account:
            return account.deposit_amount(amount)
        else:
            print("Invalid Account Number")



    def withdraw_from_account(self, amount, account_number, pin):
        account = self.account_number_validator(account_number)
        if account:
            return account.withdraw(pin, amount)
        else:
            print("Invalid Account Number")

