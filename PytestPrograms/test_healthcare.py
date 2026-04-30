'''
Task:-
Write one test case for valid patient data.
Write one test case for invalid age.
Write one test case for invalid heart rate.
Use pytest.raises(PatientValidationError, match="...").
'''
from healthcare import HealthCare , PatientValidationError
import pytest

@pytest.fixture
def patient_obj():
    return HealthCare()

def test_valid_patient_data(patient_obj):
    assert patient_obj.validate_patient(50,160)

def test_invalid_age(patient_obj):
    with pytest.raises(PatientValidationError, match = "Invalid Age"):
        patient_obj.validate_patient(130,180)

def test_invalid_heart_rate(patient_obj):
    with pytest.raises(PatientValidationError, match = "Invalid Heart rate"):
        patient_obj.validate_patient(40,10)