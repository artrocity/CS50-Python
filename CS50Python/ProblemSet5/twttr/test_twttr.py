import pytest
from twttr import shorten

def test_vowels():
    assert shorten("Hello") == "Hll"
    assert shorten("My Name is David") == "My Nm s Dvd"
    assert shorten("HELLO MY NAME IS") == "HLL MY NM S"
    assert shorten("Hello, 760") == "Hll, 760"