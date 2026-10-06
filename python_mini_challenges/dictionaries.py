"""
dictionaries.py
---------------
Python Mini Challenges: Dictionary Data Structure Operations.
Contains 5 solved dictionary problems with docstrings, type hints, and executable demos.
"""

from typing import Dict, List, Tuple, Any, Optional


def character_frequency(s: str) -> Dict[str, int]:
    """
    Problem 1: Counts the frequency of each character in a given string.
    """
    freq: Dict[str, int] = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq


def merge_dictionaries(
    dict1: Dict[Any, float], dict2: Dict[Any, float]
) -> Dict[Any, float]:
    """
    Problem 2: Merges two dictionaries. If a key exists in both, their numeric values are summed.
    """
    merged = dict(dict1)  # Copy dict1
    for key, val in dict2.items():
        merged[key] = merged.get(key, 0.0) + val
    return merged


def key_with_max_value(d: Dict[Any, float]) -> Optional[Any]:
    """
    Problem 3: Finds and returns the key associated with the maximum value in a dictionary.
    """
    if not d:
        return None
    return max(d, key=lambda k: d[k])


def calculate_student_averages(
    student_marks: Dict[str, List[float]]
) -> Dict[str, float]:
    """
    Problem 4: Given a dictionary mapping student names to lists of marks, returns average mark per student.
    Example: {'Alice': [80, 90, 85]} -> {'Alice': 85.0}
    """
    averages: Dict[str, float] = {}
    for student, marks in student_marks.items():
        if marks:
            averages[student] = round(sum(marks) / len(marks), 2)
        else:
            averages[student] = 0.0
    return averages


def group_by_category(items: List[Tuple[str, str]]) -> Dict[str, List[str]]:
    """
    Problem 5: Groups a list of tuples `(item_name, category)` into a dictionary `{category: [item_names]}`.
    """
    grouped: Dict[str, List[str]] = {}
    for name, category in items:
        cat_key = category.strip().title()
        if cat_key not in grouped:
            grouped[cat_key] = []
        grouped[cat_key].append(name.strip())
    return grouped


if __name__ == "__main__":
    print("========================================")
    print("    DICTIONARY MINI CHALLENGES DEMO")
    print("========================================")

    sample_str = "banana"
    print(f"\n1. Character Frequency ('{sample_str}'):")
    print(f"   Result: {character_frequency(sample_str)}")

    d1 = {"apple": 10, "banana": 5, "orange": 8}
    d2 = {"banana": 12, "orange": 2, "grape": 15}
    print(f"\n2. Merge Dictionaries (d1: {d1}, d2: {d2}):")
    print(f"   Result: {merge_dictionaries(d1, d2)}")

    scores = {"Alice": 88, "Bob": 95, "Charlie": 91}
    print(f"\n3. Key with Max Value ({scores}):")
    print(f"   Result: '{key_with_max_value(scores)}'")

    student_data = {
        "Neha": [85.0, 90.0, 92.5],
        "Rahul": [78.0, 82.0, 80.0],
        "Priya": [95.0, 98.0, 94.0],
    }
    print(f"\n4. Student Marks Averages:")
    print(f"   Result: {calculate_student_averages(student_data)}")

    products = [
        ("Apple", "Fruit"),
        ("Carrot", "Vegetable"),
        ("Banana", "Fruit"),
        ("Broccoli", "Vegetable"),
        ("Milk", "Dairy"),
    ]
    print(f"\n5. Group Items by Category:")
    print(f"   Result: {group_by_category(products)}")
    print("========================================")
