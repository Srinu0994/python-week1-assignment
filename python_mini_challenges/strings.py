"""
strings.py
----------
Python Mini Challenges: String Manipulation Problems.
Contains 5 solved string problems with docstrings, type hints, and executable demos.
"""

from typing import Dict


def reverse_string(s: str) -> str:
    """
    Problem 1: Reverses the given string.
    Example: 'hello' -> 'olleh'
    """
    return s[::-1]


def count_vowels(s: str) -> int:
    """
    Problem 2: Counts total vowels (a, e, i, o, u) in a string case-insensitively.
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in s if char in vowels)


def is_palindrome(s: str) -> bool:
    """
    Problem 3: Checks if a string is a palindrome, ignoring non-alphanumeric chars and case.
    Example: 'A man, a plan, a canal: Panama' -> True
    """
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]


def to_sentence_case(s: str) -> str:
    """
    Problem 4: Capitalizes the first letter of each sentence separated by periods.
    Example: 'hello world. python is great.' -> 'Hello world. Python is great.'
    """
    if not s:
        return s
    sentences = s.split(".")
    capitalized = [sentence.strip().capitalize() for sentence in sentences if sentence]
    return ". ".join(capitalized) + ("." if s.endswith(".") else "")


def word_frequency(s: str) -> Dict[str, int]:
    """
    Problem 5: Calculates the frequency of each word in a string, ignoring punctuation and case.
    """
    cleaned_chars = [char.lower() if char.isalnum() else " " for char in s]
    words = "".join(cleaned_chars).split()
    freq: Dict[str, int] = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


if __name__ == "__main__":
    print("========================================")
    print("      STRING MINI CHALLENGES DEMO")
    print("========================================")

    sample_text = "A man, a plan, a canal: Panama"
    print(f"\nOriginal String : '{sample_text}'")
    print(f"1. Reverse String  : '{reverse_string(sample_text)}'")
    print(f"2. Count Vowels     : {count_vowels(sample_text)}")
    print(f"3. Is Palindrome    : {is_palindrome(sample_text)}")

    sentence_input = "hello world. python is awesome. let us code."
    print(f"\nOriginal Sentences : '{sentence_input}'")
    print(f"4. Sentence Case    : '{to_sentence_case(sentence_input)}'")

    freq_input = "Python is great and Python is easy to learn."
    print(f"\nFrequency Input    : '{freq_input}'")
    print(f"5. Word Frequency   : {word_frequency(freq_input)}")
    print("========================================")
