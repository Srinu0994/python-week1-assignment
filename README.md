# Python Development Internship - Week 1 Assignment

**Organization**: WeIntern Pvt Ltd  
**Role**: Python Developer Intern  
**Project**: Week 1 Python Master Assignment  

---

## 📌 Executive Summary

Welcome to the **Python Development Internship - Week 1 Assignment** repository. This project is a comprehensive collection of Python solutions built for **WeIntern Pvt Ltd**, demonstrating core concepts in Python programming, Object-Oriented Programming (OOP), file I/O operations (JSON & CSV), error handling, input validation, and algorithmic problem-solving.

The codebase is organized into three distinct, modular applications designed to operate smoothly with zero runtime crashes:

1. **Student Management System** — A menu-driven command-line application featuring full CRUD capabilities, OOP principles, input validation, and persistent storage using JSON.
2. **Expense Tracker** — A financial tracking utility featuring CSV file handling, category analytics, monthly aggregations, and summary report generation.
3. **Python Mini Challenges** — A suite of 15 algorithmic challenges covering strings, lists, and dictionaries.

---

## 📁 Repository Structure

```text
python-week1-assignment/
├── student_management_system/
│   ├── main.py              # CLI menu & user interactions
│   ├── models.py            # Student & StudentManager classes
│   ├── utils.py             # Input validators & helpers
│   ├── students.json        # Persistent data file (JSON)
│   └── README.md            # Module documentation
├── expense_tracker/
│   ├── main.py              # CLI menu & user interactions
│   ├── file_handler.py      # CSV reader/writer utilities
│   ├── expenses.csv         # Persistent expense log (CSV)
│   └── README.md            # Module documentation
├── python_mini_challenges/
│   ├── strings.py           # String algorithms (5 problems)
│   ├── lists.py             # List operations & sorting (5 problems)
│   ├── dictionaries.py      # Dictionary manipulation (5 problems)
│   └── README.md            # Module documentation
├── screenshots/             # Terminal output screenshots
│   └── README.md
├── .gitignore               # Git ignore configuration
├── README.md                # Root GitHub repository handbook
└── main_README.md           # Assignment reference handbook
```

---

## 🛠️ Detailed Module Breakdown

### 1. Student Management System (`student_management_system/`)
- **Domain Modeling**: Uses `Student` dataclass/class to encapsulate student attributes (`ID`, `Name`, `Age`, `Grade`, `Marks`).
- **Data Manager**: `StudentManager` encapsulates state, JSON serialization (`students.json`), searching, updating, sorting, and analytical queries (average marks, top performer).
- **Crash Prevention**: All numerical inputs (age, marks, choices) use iterative validation loops in `utils.py` to gracefully capture `ValueError`.

### 2. Expense Tracker (`expense_tracker/`)
- **CSV Data Pipeline**: Append-mode write operations with header auto-creation to handle new installations seamlessly.
- **Analytics & Reporting**: Calculates category breakdowns, total expenditure, monthly totals, and exports structured reports (`expense_summary_report.txt`).
- **Data Integrity**: Validates dates (`YYYY-MM-DD`), positive monetary values, and category selections.

### 3. Python Mini Challenges (`python_mini_challenges/`)
- **String Processing**: Case conversion, vowel counting, palindrome verification, word frequency, and string reversing.
- **List Algorithms**: Manual selection sort implementation, order-preserving deduplication, min/max single-pass extraction, common element discovery, and parity counting.
- **Dictionary Manipulation**: Character frequency mapping, key merging with additive aggregation, score averaging, and value-based grouping.

---

## 🚀 Getting Started & Execution Instructions

### Prerequisites
- **Python 3.8+** installed on your system.
- **Git** for version control.

### Installation
Clone this repository to your local machine:
```bash
git clone https://github.com/YOUR_USERNAME/python-week1-assignment.git
cd python-week1-assignment
```

### Running the Applications

#### 1. Student Management System
```bash
python student_management_system/main.py
```

#### 2. Expense Tracker
```bash
python expense_tracker/main.py
```

#### 3. Python Mini Challenges
```bash
python python_mini_challenges/strings.py
python python_mini_challenges/lists.py
python python_mini_challenges/dictionaries.py
```

---

## 📤 Pushing to GitHub

To push your local repository changes to your remote GitHub repository:

1. **Add your GitHub repository remote** (if not already set):
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/python-week1-assignment.git
   ```
2. **Rename default branch to main**:
   ```bash
   git branch -M main
   ```
3. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Update documentation and GitHub push instructions"
   ```
4. **Push to GitHub**:
   ```bash
   git push -u origin main
   ```

---

## 🧪 Quality Assurance & Coding Standards

- **PEP 8 Compliance**: Follows standard Python naming conventions (`snake_case` functions/variables, `PascalCase` classes).
- **Error Handling**: Uses targeted exception handling (`ValueError`, `FileNotFoundError`, `KeyError`) instead of broad `except:` traps.
- **Data Persistence**: Preserves dynamic data across sessions without altering tracking schemas.

---

## 📜 License & Acknowledgments

Developed as part of the **WeIntern Python Internship Program**. All rights reserved.
