"""
file_handler.py
---------------
Handles all file I/O operations for the Expense Tracker.
Encapsulates CSV read/write operations and report export functionality.
"""

import csv
import os
from datetime import datetime
from typing import List, Dict, Any, Tuple


class ExpenseFileHandler:
    """
    Manages CSV operations for expense data persistence and file exports.
    """

    HEADERS = ["Date", "Category", "Description", "Amount"]

    def __init__(self, filename: str = "expenses.csv"):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(base_dir, filename)
        self.initialize_csv()

    def initialize_csv(self) -> None:
        """
        Creates the CSV file with headers if it does not already exist.
        """
        if not os.path.exists(self.file_path):
            try:
                with open(self.file_path, "w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(self.HEADERS)
            except IOError as e:
                print(f"Error initializing CSV file: {e}")

    def load_expenses(self) -> List[Dict[str, Any]]:
        """
        Reads all expenses from the CSV file.
        Returns a list of expense dictionaries.
        """
        if not os.path.exists(self.file_path):
            self.initialize_csv()

        expenses: List[Dict[str, Any]] = []
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for line_num, row in enumerate(reader, start=2):
                    try:
                        # Validate and parse row
                        date_str = row["Date"].strip()
                        category = row["Category"].strip()
                        description = row["Description"].strip()
                        amount = float(row["Amount"].strip())

                        # Ensure valid date format
                        datetime.strptime(date_str, "%Y-%m-%d")

                        expenses.append(
                            {
                                "Date": date_str,
                                "Category": category,
                                "Description": description,
                                "Amount": amount,
                            }
                        )
                    except (ValueError, KeyError) as e:
                        print(f"Warning: Skipping corrupted record at line {line_num}: {e}")
        except IOError as e:
            print(f"Error reading expense file: {e}")

        return expenses

    def save_expense(
        self, date_str: str, category: str, description: str, amount: float
    ) -> bool:
        """
        Appends a single new expense record to the CSV file.
        """
        try:
            with open(self.file_path, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([date_str, category, description, f"{amount:.2f}"])
            return True
        except IOError as e:
            print(f"Error appending expense to CSV file: {e}")
            return False

    def export_summary_report(
        self, summary_text: str, export_filename: str = "expense_summary_report.txt"
    ) -> Tuple[bool, str]:
        """
        Exports the summary report text to a file.
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        export_path = os.path.join(base_dir, export_filename)
        try:
            with open(export_path, "w", encoding="utf-8") as f:
                f.write(summary_text)
            return True, f"Summary report exported successfully to '{export_path}'."
        except IOError as e:
            return False, f"Failed to export summary report: {e}"
