def repeat_string(s: str, n: int) -> str:
    """Return the string `s` repeated `n` times, separated by spaces."""
    return ' '.join([s] * n)
print("repeat_string('hello', 5):")
print(repeat_string("hello", 5))  # Expected output: "hello hello hello hello hello"
print()


def first_vowel(word: str) -> str:
    """Return the first vowel in the word. Return an empty string if none."""
    vowels = 'aeiouAEIOU'
    for char in word:
        if char in vowels:
            return char
    return ''
print("Testing first_vowel('example'):")
print(first_vowel("example"))  # Expected output: "e"
print("Testing first_vowel('sky'):")
print(first_vowel("sky"))      # Expected output: ""  
print()


def is_sorted(lst: list[int]) -> bool:
    """Return True if the list is sorted in non-decreasing order, else False."""
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True
print("Testing is_sorted([1, 2, 3, 4]):")
print(is_sorted([1, 2, 3, 4]))  # Expected output: True
print("Testing is_sorted([1, 3, 2, 4]):")
print(is_sorted([1, 3, 2, 4]))  # Expected output: False
print()


def remove_duplicates(items: list[str]) -> list[str]:
    """Return a list with duplicates removed, preserving first occurrences."""
    pass
    new_list = []
    for i in items:
        if i not in new_list:
            new_list.append(i)
    return new_list
print("Testing remove_duplicates([1, 2, 2, 3, 1, 4, 5, 3]):")
print(remove_duplicates([1, 2, 2, 3, 1, 4, 5, 3]))  # Expected: [1, 2, 3, 4, 5]
print()



def fizzbuzz(n: int) -> list[str]:
    """Return a list of strings for numbers 1 to n.
    - 'Fizz' if divisible by 3
    - 'Buzz' if divisible by 5
    - 'FizzBuzz' if divisible by both
    - Otherwise, the number as a string
    """
    pass
    return [
        'FizzBuzz' if i % 15 == 0 else
        'Fizz' if i % 3 == 0 else
        'Buzz' if i % 5 == 0 else
        str(i) 
        for i in range(1, n + 1)
    ]
print("Testing fizzbuzz(10):")
print(fizzbuzz(15))  # Expected output: ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

