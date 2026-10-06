# Python Mini Challenges

A collection of 15 core algorithmic and data structure problems solved in modular Python modules.

## Objective
To master fundamental Python programming concepts, including string manipulation, list algorithms, and dictionary data structures, with type hints, detailed docstrings, and zero external dependencies.

## Structure & Modules

### 1. `strings.py` (String Challenges)
- `reverse_string`: Reverses string characters.
- `count_vowels`: Counts vowels (a, e, i, o, u) case-insensitively.
- `is_palindrome`: Palindrome check ignoring non-alphanumeric characters and case.
- `to_sentence_case`: Capitalizes initial letter of sentences.
- `word_frequency`: Calculates word frequency distribution in text.

### 2. `lists.py` (List Challenges)
- `find_largest_and_smallest`: Finds max and min values in a single pass.
- `remove_duplicates`: Deduplicates lists while preserving insertion order.
- `custom_sort`: Selection Sort implementation without using `.sort()` or `sorted()`.
- `find_common_elements`: Identifies unique common items across two lists.
- `count_even_odd`: Returns counts of even and odd integers.

### 3. `dictionaries.py` (Dictionary Challenges)
- `character_frequency`: Frequency counter for string characters.
- `merge_dictionaries`: Merges dictionaries with additive value handling for common keys.
- `key_with_max_value`: Retrieves key corresponding to maximum value.
- `calculate_student_averages`: Computes mean score per student from mark lists.
- `group_by_category`: Groups key-category pairs into category buckets.

## How to Run

Run each module individually to execute its demo suite:

```bash
# Run String Challenges
python python_mini_challenges/strings.py

# Run List Challenges
python python_mini_challenges/lists.py

# Run Dictionary Challenges
python python_mini_challenges/dictionaries.py
```

## Sample Output

```text
========================================
      STRING MINI CHALLENGES DEMO
========================================

Original String : 'A man, a plan, a canal: Panama'
1. Reverse String  : 'amanaP :lanac a ,nalp a ,nam A'
2. Count Vowels     : 10
3. Is Palindrome    : True

Original Sentences : 'hello world. python is awesome. let us code.'
4. Sentence Case    : 'Hello world. Python is awesome. Let us code.'

Frequency Input    : 'Python is great and Python is easy to learn.'
5. Word Frequency   : {'python': 2, 'is': 2, 'great': 1, 'and': 1, 'easy': 1, 'to': 1, 'learn': 1}
========================================
```

## Author
- **Author**: [Your Name]
- **Role**: Python Developer Intern (WeIntern Pvt Ltd)
