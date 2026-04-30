import pytest

# Challenge 1: The "Assert" master
'''
In unittest (the old way), you had to remember self.assertEqual(). In pytest, you just use assert.
'''

def test_string_methods():
    assert "pytest".startswith("p") 
    assert len([1,2,3]) == 3
    assert "hello".capitalize() == "Hello"


# Challenge 2: Testing for Failures
'''
Sometimes, you want to make sure your code fails correctly. For example, dividing by zero should raise an error.
'''

def divide(a,b):
    return a/b

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)

# to run test on particular file python -m pytest test_file_name.py -v for more clearity (-v stands for verbose)

# Challenge 3: The "Membership" and "Identity" Tests
'''
In Python, we often check if something exists inside a collection or if a condition is True/False.
'''
def test_list_contains():
    assert 5 in [1,3,5,7]

def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
    
def test_is_even():
    assert is_even(4) # or assert is_even(4) is True