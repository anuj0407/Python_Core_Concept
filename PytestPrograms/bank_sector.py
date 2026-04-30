'''
Question 4: Banking Sector
Scenario:-
Create a function transfer(from_account, to_account, amount, balance).
Account numbers must follow a valid format such as 10 digits.
Transfer amount must be greater than 0.
Transfer amount must not be greater than balance.
Raise TransferError for invalid cases.

Task:-
Write one test case for successful transfer.
Write one test case for zero amount.
Write one test case for insu cient balance.
Write one test case for invalid account number.
Use regex for account validation.
Use pytest.raises() for exception testing.
'''
import re
#custom exception
class TransferError(Exception):
    pass

class Bank:
    def transfer(self,from_account, to_account, amount, balance):
        account_no_pattern = r"^\d{10}$"
        if not re.match(account_no_pattern,from_account):
            raise TransferError("Invalid Account number")
        elif not re.match(account_no_pattern,to_account):
            raise TransferError("Invalid Account number")
        elif amount <= 0:
            raise TransferError("Invalid amount i.e. amount cannot be negative or zero")
        elif amount > balance:
            raise TransferError("Invalid amount i.e. Insufficient balance")
        else:
            return True
