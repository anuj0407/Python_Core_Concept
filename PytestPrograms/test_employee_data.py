'''
Task:-
Write one test case for valid employee ID and email.
Write one test case for invalid employee ID like EMP-12.
Write one test case for invalid email like john@gmail.com
Use regex for validation.
Use pytest.raises() for invalid input.
'''
from employee_data import Employee
import pytest

@pytest.fixture
def employee_obj():
    return Employee()

def test_valid_emp_id_and_email(employee_obj):
    assert employee_obj.validate_employee("EMP-1024","Anuj@Neo.com")

def test_invalid_emp_id(employee_obj):
    with pytest.raises(ValueError,match = "Invalid Employee Id"):
        employee_obj.validate_employee("EMP-12","Rahul@gla.com")

def test_invalid_email(employee_obj):
    with pytest.raises(ValueError,match = "Invalid Email"):
        employee_obj.validate_employee("EMP-1027","john@gmail.com")
