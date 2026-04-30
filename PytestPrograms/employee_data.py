'''Question 2: Employee Data
Scenario:-
Create a function validate_employee(emp_id, email).
Employee ID format must be EMP-1234.
Email format must be name@company.com.
If ID is invalid, raise ValueError.
If email is invalid, raise ValueError.

Task:-
Write one test case for valid employee ID and email.
Write one test case for invalid employee ID like EMP-12.
Write one test case for invalid email like john@gmail.com
Use regex for validation.
Use pytest.raises() for invalid input.'''
import re

class Employee:

    def validate_employee(self,emp_id,email):
        id_pattern = r"^EMP-\d{4}$"
        email_pattern = r"^[A-Za-z0-9]+@(?!gmail\.com$)[A-Za-z0-9]+\.com$"

        if re.match(id_pattern,emp_id):
            if(re.match(email_pattern,email)):
                return True
            else:
                raise ValueError("Invalid Email")
        else:
            raise ValueError("Invalid Employee Id")


