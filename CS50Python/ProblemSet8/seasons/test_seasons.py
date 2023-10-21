import pytest
from datetime import date
from seasons import check_dob

def main():
    test_check_dob()
    test_invalid_dob()

#defining a fixture to provide a valid date of birth
@pytest.fixture
def valid_dob():
    return "2022-09-05"

#defining a fixture to provide an invalid date of birth
@pytest.fixture
def invalid_dob():
    return "Invalid Date"

#Using check_dob function to check the valid dob fixture
def test_check_dob(valid_dob):
    expected_date = date(2022, 9, 5)
    result = check_dob(valid_dob)
    assert result == expected_date

#Using check_dob function to check the invalid dob fixture
def test_invalid_dob(invalid_dob):
    with pytest.raises(SystemExit):
        check_dob(invalid_dob)
