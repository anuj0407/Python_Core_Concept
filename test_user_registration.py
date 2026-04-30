import re
import pytest

class UserValidator:
    def validate_email(self, email):
        if not isinstance(email, str):
            raise TypeError("Email must be a string")
        
        # Simple regex for email: alphanumeric@://alphanumeric.com
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(re.match(pattern, email))

'''The Task: Write three tests for the validate_email method.
One test for a valid email (should return True).
One test for an invalid email (should return False).
One test to ensure it raises a TypeError if you pass a number instead of a string.'''

@pytest.fixture
def validator():
    return UserValidator()

def test_valid_email(validator):
    assert validator.validate_email("anuj@gmail.com")

def test_invalid_email(validator):
    assert validator.validate_email("anuj.com") is False # or == False

def test_Error(validator):
    with pytest.raises(TypeError):
        validator.validate_email(232)

# To do multiple test
# define the variable name as a string , then pass a list of values
@pytest.mark.parametrize("email",["plainaddress", 
    "#@%^%#$@#$@#.com", 
    "@example.com", 
    "joe smith@example.com"])

def test_multiple_invalid_emails(validator,email):
    assert validator.validate_email(email) is False 