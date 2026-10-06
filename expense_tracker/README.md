# Expense Tracker

A CLI application for tracking personal expenses, logging data to CSV files, and generating analytical summary reports.

## Objective
To provide a clean, reliable command-line tool for recording daily expenses, categorizing spending, inspecting financial metrics, and handling file operations safely without exceptions or tracebacks.

## Features
- **Core Functionality**:
  - **Add Expense**: Record date (YYYY-MM-DD), category, description, and amount.
  - **View All**: Neatly formatted table showing all recorded expenses.
  - **Category Filter**: Search and summarize expenses by category (e.g., Food, Travel, Utilities).
  - **CSV File Persistence**: Saves each record in append mode to `expenses.csv` with automated header initialization.
  - **Safe Path Handling**: Avoids overwriting existing files and uses absolute relative paths via `os.path`.
- **Enhancements & Analytics**:
  - **Summary Report**: Shows total entries, total spent, highest expense record, and category-wise percentage breakdown.
  - **Monthly Summary**: Group expenses by month (`YYYY-MM`).
  - **Sorting**: Order expenses by amount (High-to-Low or Low-to-High).
  - **Report Export**: Export formatted summary report to `expense_summary_report.txt`.
- **Robust Exception Handling**: Custom validation for invalid dates, non-numeric amounts, missing files, and empty fields.

## Technologies Used
- Python 3.10+
- Built-in `csv`, `os`, `sys`, and `datetime` modules

## Folder Structure
```text
expense_tracker/
├── main.py          # Interactive menu loop and input handler
├── file_handler.py  # File IO module for CSV reading/writing & exports
├── expenses.csv     # Persistent CSV data storage
└── README.md        # Documentation
```

## How to Run
From the repository root or directory, run:
```bash
python expense_tracker/main.py
```

## Sample Input and Output

### Sample Run 1: Viewing Summary Report
```text
========================================
         ===== Expense Summary =====
========================================
Total Entries   : 6
Total Spent     : 4620.50
Highest Expense : Utilities - 1850.00 (Electricity Bill)
----------------------------------------
Category-wise Breakdown:
  - Utilities      :  1850.00 ( 40.0%)
  - Travel         :  1520.00 ( 32.9%)
  - Food           :   800.50 ( 17.3%)
  - Entertainment  :   450.00 (  9.7%)
========================================
```

### Sample Run 2: Exporting Report
```text
Enter your choice (1-8): 7
 Summary report exported successfully to 'expense_tracker/expense_summary_report.txt'.
```

## Author
- **Author**: [Your Name]
- **Role**: Python Developer Intern (WeIntern Pvt Ltd)
