import pytest
from working import convert

def main():
    test_format()
    test_errors()

def test_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("09:30 AM to 5:30 PM") == "09:30 to 17:30"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"

def test_errors():
    with pytest.raises(ValueError):
        convert("9AM - 5PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")
    with pytest.raises(ValueError):
        convert("14 PM to 21 PM")
    with pytest.raises(ValueError):
        convert("8AM 9 AM")
    with pytest.raises(ValueError):
        convert("08:61 AM to 09:61")