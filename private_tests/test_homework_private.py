import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from homework import repeat_string, first_vowel, is_sorted, remove_duplicates, fizzbuzz

# Tests for repeat_string
def test_repeat_string_private_1():
    assert repeat_string("hello", 2) == "hello hello"

def test_repeat_string_private_2():
    assert repeat_string("x", 5) == "x x x x x"

def test_repeat_string_private_3():
    assert repeat_string("abc", 0) == ""

# Tests for first_vowel
def test_first_vowel_private_1():
    assert first_vowel("strength") == "e"

def test_first_vowel_private_2():
    assert first_vowel("queue") == "u"

def test_first_vowel_private_3():
    assert first_vowel("rhythm") == ""

# Tests for is_sorted
def test_is_sorted_private_1():
    assert is_sorted([1, 3, 5, 7])

def test_is_sorted_private_2():
    assert not is_sorted([5, 4, 3, 2])

def test_is_sorted_private_3():
    assert is_sorted([10])

# Tests for remove_duplicates
def test_remove_duplicates_private_1():
    assert remove_duplicates(["one", "two", "one", "three", "two"]) == ["one", "two", "three"]

def test_remove_duplicates_private_2():
    assert remove_duplicates(["apple", "banana", "apple", "apple"]) == ["apple", "banana"]

def test_remove_duplicates_private_3():
    assert remove_duplicates(["dog", "cat", "bird", "cat", "dog", "dog"]) == ["dog", "cat", "bird"]

# Tests for fizzbuzz
def test_fizzbuzz_private_1():
    assert fizzbuzz(3) == ["1", "2", "Fizz"]

def test_fizzbuzz_private_2():
    assert fizzbuzz(6) == ["1", "2", "Fizz", "4", "Buzz", "Fizz"]

def test_fizzbuzz_private_3():
    assert fizzbuzz(15)[-1] == "FizzBuzz"
