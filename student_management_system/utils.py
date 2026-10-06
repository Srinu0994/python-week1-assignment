"""
utils.py
--------
Utility and helper functions for input validation and formatting in the Student Management System.
Prevents program crashes by handling invalid inputs gracefully.
"""

from typing import Optional


def get_valid_int(
    prompt: str,
    min_val: Optional[int] = None,
    max_val: Optional[int] = None,
    allow_empty: bool = False,
) -> Optional[int]:
    """
    Prompts the user for an integer input and validates it against range limits.
    """
    while True:
        user_input = input(prompt).strip()
        if allow_empty and not user_input:
            return None

        try:
            val = int(user_input)
            if min_val is not None and val < min_val:
                print(f" Invalid input: Value must be at least {min_val}.")
                continue
            if max_val is not None and val > max_val:
                print(f" Invalid input: Value must be at most {max_val}.")
                continue
            return val
        except ValueError:
            print(" Invalid input: Please enter a valid integer.")


def get_valid_float(
    prompt: str,
    min_val: Optional[float] = None,
    max_val: Optional[float] = None,
    allow_empty: bool = False,
) -> Optional[float]:
    """
    Prompts the user for a float input and validates it against range limits.
    """
    while True:
        user_input = input(prompt).strip()
        if allow_empty and not user_input:
            return None

        try:
            val = float(user_input)
            if min_val is not None and val < min_val:
                print(f" Invalid input: Value must be at least {min_val}.")
                continue
            if max_val is not None and val > max_val:
                print(f" Invalid input: Value must be at most {max_val}.")
                continue
            return val
        except ValueError:
            print(" Invalid input: Please enter a valid numeric value.")


def get_non_empty_string(prompt: str, allow_empty: bool = False) -> Optional[str]:
    """
    Prompts the user for a string input and ensures it is non-empty.
    """
    while True:
        user_input = input(prompt).strip()
        if allow_empty and not user_input:
            return None
        if user_input:
            return user_input
        print(" Invalid input: Field cannot be empty.")


def get_yes_no(prompt: str) -> bool:
    """
    Prompts for a Yes/No confirmation.
    """
    while True:
        response = input(f"{prompt} (y/n): ").strip().lower()
        if response in ("y", "yes"):
            return True
        elif response in ("n", "no"):
            return False
        print(" Please enter 'y' for Yes or 'n' for No.")
