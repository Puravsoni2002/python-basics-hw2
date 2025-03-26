import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from homework import repeat_string, first_vowel, is_sorted, remove_duplicates, fizzbuzz

def test_repeat_string():
    assert repeat_string("hi", 3) == "hi hi hi"
    assert repeat_string("a", 1) == "a"
    assert repeat_string("ok", 0) == ""

def test_first_vowel():
    assert first_vowel("apple") == "a"
    assert first_vowel("try") == ""
    assert first_vowel("sky") == ""

def test_is_sorted():
    assert is_sorted([1, 2, 2, 3])
    assert not is_sorted([3, 1, 2])
    assert is_sorted([])

def test_remove_duplicates():
    assert remove_duplicates(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]
    assert remove_duplicates([]) == []
    assert remove_duplicates(["a", "a", "a"]) == ["a"]

def test_fizzbuzz():
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizzbuzz(1) == ["1"]
    assert fizzbuzz(0) == []
