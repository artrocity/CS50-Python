from um import count
import pytest

def main():
    test_case_sensitivity()
    test_spaces()
    test_punctuation()
    test_words()

def test_case_sensitivity():
    assert count("um") == 1
    assert count("UM") == 1

def test_spaces():
    assert count("um") == 1
    assert count(" um ") == 1

def test_punctuation():
    assert count("Hello um?") == 1
    assert count("!um!") == 1

def test_words():
    assert count("I am yum bum rum um") == 1

if __name__ == "__main__":
    main()