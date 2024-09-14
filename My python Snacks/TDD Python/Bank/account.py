
class Account:

    def __init__(self, account_name, pin, balance, account_number ):
        self.name = account_name
        self.pin = pin
        self.balance = balance
        self.account_number = account_number

    def deposit_amount(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    def pin_valid_is_valid(self, pin):
        if self.pin != pin:
            return False
        if self.pin == pin:
            return True

    def get_account_balance(self, pin):
         if self.pin_valid_is_valid(pin):
             return self.balance


    def withdraw(self, pin, amount):
        if self.pin_valid_is_valid(pin) and self.balance > amount:
            self.balance = self.balance - amount
            return self.balance

        elif self.pin_valid_is_valid(pin):
            println: "invalid pin"



    def get_name(self):
        return self.name


    def get_pin(self):
        return self.pin


    def get_account_number(self):
        return self.account_number

