from fuel import convert
from fuel import gauge
import pytest

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert convert("1/4") == 25
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ValueError):
        convert("5/4")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(30) == "30%"
    assert gauge (99) == "F"