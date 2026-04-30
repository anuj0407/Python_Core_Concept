'''
Task:-
Write one test case for input like John Doe!.
Write one test case for input like !@#$%.
Write one test case for input like Payment: 100$.
Check cleaned output for valid text.
Check exception for empty cleaned text.
'''
from regex_and_exception import InputSanitizationError , CleanText
import pytest

@pytest.fixture
def clean_text_obj():
    return CleanText()

def test_valid_input(clean_text_obj):
    assert clean_text_obj.sanitize_input("John Doe!") == "John Doe"

def test_invalid_input(clean_text_obj):
    with pytest.raises(InputSanitizationError,match = "Empty string left after cleaning special character"):
        clean_text_obj.sanitize_input("!@#$%")

def test_another_valid_input(clean_text_obj):
    assert clean_text_obj.sanitize_input("Payment: 100$") == "Payment 100"
