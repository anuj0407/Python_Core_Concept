import re
import pytest

class PasswordHasher:
    def validate_password(self, password):
        if not isinstance(password, str):
            raise ValueError("Password must be a string")
            
        # Regex: Lookahead for at least one digit and one special char
        # Minimum 8 characters total
        pattern = r"^(?=.*[0-9])(?=.*[@$!%*?&])[A-Za-z0-9@$!%*?&]{8,}$"
        
        return bool(re.match(pattern, password))


@pytest.fixture
def hasher():
    return PasswordHasher()

@pytest.mark.parametrize("password",["Python@123","Secure!99","Admin$2024","Anuj@2ch"])
def test_multiple_valid_password(hasher,password):
    assert hasher.validate_password(password)

@pytest.mark.parametrize("password",["abA@","pass!word","Hello230"])
def test_multiple_invalid_password(hasher,password):
    assert hasher.validate_password(password) is False

def test_error(hasher):
    with pytest.raises(ValueError):
        hasher.validate_password(12345678)