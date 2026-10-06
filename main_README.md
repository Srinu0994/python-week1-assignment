# Python Development Internship - Week 1 Assignment Handbook
**Organization**: WeIntern Pvt Ltd  
**Author**: [Your Name]  
**Role**: Python Developer Intern  

---

## 📌 Executive Summary

This repository contains the complete Week 1 Python Development Internship project submission for **WeIntern Pvt Ltd**. It consists of three modular, robust, and crash-proof Python applications:

1. **Student Management System** (Object-Oriented CRUD & JSON persistence)
2. **Expense Tracker** (CSV File Handling & Expense Analytics)
3. **Python Mini Challenges** (15 Algorithmic solutions across strings, lists, and dictionaries)

---

## 📁 Recommended Repository Structure

```text
python-week1-assignment/
├── student_management_system/
│   ├── main.py
│   ├── models.py
│   ├── utils.py
│   └── README.md
├── expense_tracker/
│   ├── main.py
│   ├── expenses.csv
│   ├── file_handler.py
│   └── README.md
├── python_mini_challenges/
│   ├── strings.py
│   ├── lists.py
│   ├── dictionaries.py
│   └── README.md
├── screenshots/
│   └── README.md
├── .gitignore
└── main_README.md
```

---

## 🛠️ Tasks Breakdown & Highlights

### Task 1: Student Management System (Console, Menu-Driven, OOP)
- **Architecture**: Separated into `models.py` (OOP domain model & manager), `utils.py` (input validators), and `main.py` (CLI interface).
- **Core Features**:
  - Full CRUD: Unique ID checking, formatted string displays, partial updates, and deletion confirmation.
  - Advanced Features: JSON file storage (`students.json`), sorting by marks/name, class average calculations, and top-performer identification.

### Task 2: Expense Tracker (Console, File Handling)
- **Architecture**: Separated file I/O operations in `file_handler.py` from menu orchestration in `main.py`.
- **Core Features**:
  - Safe CSV handling using append mode, automatic header generation, and safe path resolution.
  - Analytics & Reports: Category breakdown, monthly aggregations, sorting by amount, and exporting summary reports to file (`expense_summary_report.txt`).

### Task 3: Python Mini Challenges (Algorithmic Fundamentals)
- **`strings.py`**: Reverse string, count vowels, palindrome checker, sentence case converter, word frequency.
- **`lists.py`**: Max/Min pass, deduplication with order retention, custom Selection Sort algorithm, common elements finder, even/odd counter.
- **`dictionaries.py`**: Character frequency counter, dictionary merger with additive values, max value key finder, student score mean calculator, category grouper.

---

## 🚀 Execution Instructions

Run each component from the repository root:

```bash
# 1. Run Student Management System
python student_management_system/main.py

# 2. Run Expense Tracker
python expense_tracker/main.py

# 3. Run Python Mini Challenges
python python_mini_challenges/strings.py
python python_mini_challenges/lists.py
python python_mini_challenges/dictionaries.py
```

---

## 🧪 Testing & Validation Criteria

- ✅ **No Broad Exception Traps**: Specific exceptions (`ValueError`, `FileNotFoundError`, `KeyError`) used everywhere.
- ✅ **Input Validation**: All integer, float, string, and date inputs are validated iteratively to prevent runtime crashes.
- ✅ **Data Persistence**: Records persist across app restarts (`students.json` & `expenses.csv`).
- ✅ **PEP 8 Compliance**: Written strictly in `snake_case` for variables/functions and `PascalCase` for classes.

---

## 📸 Screenshots
Refer to [`screenshots/README.md`](screenshots/README.md) for terminal screenshot guidelines and placement details.
