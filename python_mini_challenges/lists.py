"""
lists.py
--------
Python Mini Challenges: List Processing & Algorithms.
Contains 5 solved list problems with docstrings, type hints, and executable demos.
"""

from typing import List, Tuple, Dict, Any


def find_largest_and_smallest(numbers: List[float]) -> Tuple[float, float]:
    """
    Problem 1: Returns the largest and smallest numbers in a list without crashing on single/empty lists.
    """
    if not numbers:
        raise ValueError("List cannot be empty.")

    largest = numbers[0]
    smallest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return largest, smallest


def remove_duplicates(items: List[Any]) -> List[Any]:
    """
    Problem 2: Removes duplicate elements from a list while preserving original insertion order.
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def custom_sort(numbers: List[float], reverse: bool = False) -> List[float]:
    """
    Problem 3: Sorts a numeric list using Selection Sort algorithm without relying on built-in sort() or sorted().
    """
    arr = list(numbers)  # Create a shallow copy
    n = len(arr)
    for i in range(n):
        target_idx = i
        for j in range(i + 1, n):
            if reverse:
                if arr[j] > arr[target_idx]:
                    target_idx = j
            else:
                if arr[j] < arr[target_idx]:
                    target_idx = j
        arr[i], arr[target_idx] = arr[target_idx], arr[i]
    return arr


def find_common_elements(list1: List[Any], list2: List[Any]) -> List[Any]:
    """
    Problem 4: Returns a list of unique common elements present in both list1 and list2.
    """
    set2 = set(list2)
    common = []
    seen = set()
    for item in list1:
        if item in set2 and item not in seen:
            seen.add(item)
            common.append(item)
    return common


def count_even_odd(numbers: List[int]) -> Dict[str, int]:
    """
    Problem 5: Counts the number of even and odd integers in a list.
    """
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return {"even": even_count, "odd": odd_count}


if __name__ == "__main__":
    print("========================================")
    print("       LIST MINI CHALLENGES DEMO")
    print("========================================")

    nums = [45, 12, 89, 12, 3, 99, 45, 23]
    print(f"\nOriginal List       : {nums}")

    max_val, min_val = find_largest_and_smallest(nums)
    print(f"1. Largest & Smallest : Largest = {max_val}, Smallest = {min_val}")

    unique_items = remove_duplicates(nums)
    print(f"2. Remove Duplicates  : {unique_items}")

    sorted_asc = custom_sort(nums, reverse=False)
    sorted_desc = custom_sort(nums, reverse=True)
    print(f"3. Custom Sort (Asc)  : {sorted_asc}")
    print(f"   Custom Sort (Desc) : {sorted_desc}")

    a = [1, 2, 3, 4, 5, 6]
    b = [4, 5, 6, 7, 8, 9]
    print(f"\nList A: {a} | List B: {b}")
    print(f"4. Common Elements   : {find_common_elements(a, b)}")

    int_sample = [10, 21, 32, 43, 54, 65, 76, 87]
    print(f"\nIntegers List       : {int_sample}")
    print(f"5. Even/Odd Counts   : {count_even_odd(int_sample)}")
    print("========================================")
