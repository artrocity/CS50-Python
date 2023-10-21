import pytest
from bank import value

def main():
    test_hello()
    test_hi()
    test_other()

def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0

def test_hi():
    assert value("hi") == 20

def test_other():
    assert value("Nice to meet you") == 100



