from jar import Jar
import pytest

def test_init():
    capacity = 5
    jar = Jar(capacity)
    assert jar.max_capacity == capacity


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"
    with pytest.raises(ValueError):
        jar.deposit(20)

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
