from e_commerce import Ecom
import pytest

@pytest.fixture
def calculate():
    return Ecom()

def test_valid_item_prices_and_tax_rate(calculate):
    assert calculate.calculate_total([100,200,400,250],0.2) == 951.90

def test_invalid_price(calculate):
    with pytest.raises(ValueError, match = "Price can not be negative"):
        calculate.calculate_total([-200,100,-300],0.5)

def test_invalid_tax_rate(calculate):
    with pytest.raises(ValueError, match = "Tax rate must be in range"):
        calculate.calculate_total([100,200,500,600],3)
