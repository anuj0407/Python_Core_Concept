import pytest

def convert_to_int(val):
    return int(val)

def test_invalid_input():
    with pytest.raises(ValueError):
        convert_to_int("abc")