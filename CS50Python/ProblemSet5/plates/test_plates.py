from plates import is_valid
import pytest

def main():
    test_alpha()
    test_alphanumeric()
    test_number()
    test_length()

def test_alpha():
    assert is_valid("qwerty") == True
    assert is_valid("12qwe") == False

def test_alphanumeric():
    assert is_valid("qwe,") == False

def test_number():
    assert is_valid("qwe12") == True
    assert is_valid("qw0") == False
    assert is_valid("12") == False
    assert is_valid("qw50s") == False

def test_length():
    assert is_valid("qwe") == True
    assert is_valid("q") == False