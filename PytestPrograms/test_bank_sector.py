'''
Task:-
Write one test case for successful transfer.
Write one test case for zero amount.
Write one test case for insu cient balance.
Write one test case for invalid account number.
Use regex for account validation.
Use pytest.raises() for exception testing.
'''
from bank_sector import Bank , TransferError
import pytest

@pytest.fixture
def bank_obj():
    return Bank()

def test_valid_transfer(bank_obj):
    assert bank_obj.transfer("3189442729","3152913811",10000,50000)

def test_invalid_amount(bank_obj):
    with pytest.raises(TransferError,match = "Invalid amount i.e. amount cannot be negative or zero"):
        bank_obj.transfer("3189201292","8927138311",0,10000)

def test_insufficient_balance(bank_obj):
    with pytest.raises(TransferError , match = "Invalid amount i.e. Insufficient balance"):
        bank_obj.transfer("3214582934","2138749392",100000,5000)

def test_invalid_account_no(bank_obj):
    with pytest.raises(TransferError, match = "Invalid Account number"):
        bank_obj.transfer("323213","1344553353",10000,30000)

