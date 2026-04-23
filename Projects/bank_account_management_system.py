'''
Creating a system where we have a general account and a specialized "Savings" account.
we need to protect the balance and ensure certain rules are followed. 
'''

class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.__balance = 0

    @property
    def total_balance(self):
        return self.__balance
    
    @total_balance.setter
    def total_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Enter a valid balance")

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.__balance = self.__balance + deposit_amount
            print(f"Your account has been credited with {deposit_amount} , current balance is {self.__balance}")
        else:
            print("Enter a valid amount to deposit")
        
    def withdraw(self, withdraw_amount):
        if withdraw_amount > 0 :
            if self.__balance >= withdraw_amount:
                self.__balance = self.__balance - withdraw_amount
                print(f"Your account has been debited with {withdraw_amount} , current balance is {self.__balance}")
            else:
                print("Insufficient balance")
        else:
            print("Enter a valid amount to withdraw")

    def __str__(self):
        return f"Account holder: {self.account_holder}, Balance: {self.__balance}"

class SavingAccount(BankAccount):
    def __init__(self,account_holder,account_number):
        self.account_number = account_number
        super().__init__(account_holder)
        self._interest_rate = 0.03  #Interest rate is 3%

    def apply_interest(self):
        self.__balance = self.total_balance * (1+self._interest_rate)
        self.total_balance = self.__balance



# User interaction
print("------Welcome to the Bank Account Management System------")
my_account = SavingAccount("Anuj","12402341")
my_account.deposit(10000)
my_account.apply_interest()
print(f"Current balance is {my_account.total_balance}") # using the getter method
my_account.withdraw(5000)
print(my_account) # by using __str__ method
