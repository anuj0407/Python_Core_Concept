'''
Question 3: Healthcare
Scenario
Create a custom exception called PatientValidationError.
Create a function validate_patient(age, heart_rate).
Age must be between 0 and 120.
Heart rate must be between 20 and 220.
Raise PatientValidationError for invalid values.

Task:-
Write one test case for valid patient data.
Write one test case for invalid age.
Write one test case for invalid heart rate.
Use pytest.raises(PatientValidationError, match="...").
'''

# custom exception
class PatientValidationError(Exception):
    pass

class HealthCare:
    def validate_patient(self, age, heart_rate):
        if not 0 < age < 120:
            raise PatientValidationError("Invalid Age")
        elif not 20 < heart_rate < 220:
            raise PatientValidationError("Invalid Heart rate")
        else:
            return True
        
