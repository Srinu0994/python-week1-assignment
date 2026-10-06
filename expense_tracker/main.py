"""
main.py
-------
Console entry point for the Expense Tracker application.
Provides a interactive, menu-driven CLI interface with CSV persistence and analytical reports.
"""

import sys
from datetime import datetime
from typing import List, Dict, Any
from file_handler import ExpenseFileHandler


def get_valid_date(prompt: str) -> str:
    """
    Prompts the user for a date string in YYYY-MM-DD format or allows pressing enter for today.
    """
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            # Default to current date
            return datetime.now().strftime("%Y-%m-%d")

        try:
            valid_date = datetime.strptime(user_input, "%Y-%m-%d")
            return valid_date.strftime("%Y-%m-%d")
        except ValueError:
            print(" Invalid date format. Please enter date in YYYY-MM-DD format (e.g. 2026-10-06).")


def get_non_empty_string(prompt: str) -> str:
    """Prompts for a non-empty string."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print(" Invalid input: Field cannot be empty.")


def get_valid_amount(prompt: str) -> float:
    """Prompts for a positive float amount."""
    while True:
        user_input = input(prompt).strip()
        try:
            amount = float(user_input)
            if amount <= 0:
                print(" Invalid input: Amount must be greater than zero.")
                continue
            return amount
        except ValueError:
            print(" Invalid input: Please enter a valid number for amount.")


def display_menu() -> None:
    """Displays main menu options."""
    print("\n" + "=" * 45)
    print("        ===== Expense Tracker =====")
    print("=" * 45)
    print("  1. Add Expense")
    print("  2. View All Expenses")
    print("  3. Filter Expenses by Category")
    print("  4. View Summary Report")
    print("  5. View Monthly Breakdown (Enhancement)")
    print("  6. Sort Expenses by Amount (Enhancement)")
    print("  7. Export Summary Report (Enhancement)")
    print("  8. Exit")
    print("=" * 45)


def handle_add_expense(handler: ExpenseFileHandler) -> None:
    """Handles adding a new expense entry."""
    print("\n--- Add New Expense ---")
    date_str = get_valid_date("Enter Date (YYYY-MM-DD) [Press Enter for Today]: ")
    category = get_non_empty_string("Enter Category (e.g., Food, Travel, Utilities): ").title()
    description = get_non_empty_string("Enter Short Description: ")
    amount = get_valid_amount("Enter Amount (e.g., 250.50): ")

    success = handler.save_expense(date_str, category, description, amount)
    if success:
        print(f" Expense of {amount:.2f} under '{category}' recorded successfully.")
    else:
        print(" Error: Failed to save expense record.")


def handle_view_all(handler: ExpenseFileHandler) -> None:
    """Displays all expense records."""
    expenses = handler.load_expenses()
    print("\n--- All Expenses ---")
    if not expenses:
        print(" No expense records found.")
        return

    print("-" * 70)
    print(f"{'Date':<12} | {'Category':<15} | {'Description':<25} | {'Amount':>8}")
    print("-" * 70)
    total = 0.0
    for exp in expenses:
        print(f"{exp['Date']:<12} | {exp['Category']:<15} | {exp['Description']:<25} | {exp['Amount']:>8.2f}")
        total += exp["Amount"]
    print("-" * 70)
    print(f"Total Entries: {len(expenses)} | Total Spent: {total:.2f}")


def handle_filter_by_category(handler: ExpenseFileHandler) -> None:
    """Filters expenses by category name."""
    expenses = handler.load_expenses()
    if not expenses:
        print(" No expense records found.")
        return

    category_query = get_non_empty_string("Enter Category to filter: ").strip().lower()
    filtered = [e for e in expenses if e["Category"].lower() == category_query]

    print(f"\n--- Expenses under '{category_query.title()}' ---")
    if not filtered:
        print(f" No records found for category '{category_query.title()}'.")
        return

    print("-" * 70)
    print(f"{'Date':<12} | {'Category':<15} | {'Description':<25} | {'Amount':>8}")
    print("-" * 70)
    cat_total = 0.0
    for exp in filtered:
        print(f"{exp['Date']:<12} | {exp['Category']:<15} | {exp['Description']:<25} | {exp['Amount']:>8.2f}")
        cat_total += exp["Amount"]
    print("-" * 70)
    print(f"Category Total ({len(filtered)} entries): {cat_total:.2f}")


def generate_summary_text(expenses: List[Dict[str, Any]]) -> str:
    """Generates a formatted summary text block."""
    if not expenses:
        return "No expenses recorded."

    total_entries = len(expenses)
    total_spent = sum(e["Amount"] for e in expenses)
    highest_expense = max(expenses, key=lambda e: e["Amount"])

    category_totals: Dict[str, float] = {}
    for e in expenses:
        cat = e["Category"]
        category_totals[cat] = category_totals.get(cat, 0.0) + e["Amount"]

    lines = [
        "========================================",
        "         ===== Expense Summary =====",
        "========================================",
        f"Total Entries   : {total_entries}",
        f"Total Spent     : {total_spent:.2f}",
        f"Highest Expense : {highest_expense['Category']} - {highest_expense['Amount']:.2f} ({highest_expense['Description']})",
        "----------------------------------------",
        "Category-wise Breakdown:",
    ]
    for cat, amt in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
        pct = (amt / total_spent * 100) if total_spent > 0 else 0
        lines.append(f"  - {cat:<15}: {amt:>8.2f} ({pct:>5.1f}%)")
    lines.append("========================================")

    return "\n".join(lines)


def handle_summary_report(handler: ExpenseFileHandler) -> None:
    """Displays the summary report."""
    expenses = handler.load_expenses()
    if not expenses:
        print(" No expense records found.")
        return

    summary_text = generate_summary_text(expenses)
    print("\n" + summary_text)


def handle_monthly_summary(handler: ExpenseFileHandler) -> None:
    """Displays monthly breakdown of expenses."""
    expenses = handler.load_expenses()
    if not expenses:
        print(" No expense records found.")
        return

    monthly_totals: Dict[str, float] = {}
    monthly_counts: Dict[str, int] = {}
    for e in expenses:
        month_key = e["Date"][:7]  # YYYY-MM
        monthly_totals[month_key] = monthly_totals.get(month_key, 0.0) + e["Amount"]
        monthly_counts[month_key] = monthly_counts.get(month_key, 0) + 1

    print("\n--- Monthly Expense Breakdown ---")
    print("-" * 45)
    print(f"{'Month (YYYY-MM)':<18} | {'Entries':<8} | {'Total Spent':>12}")
    print("-" * 45)
    for m in sorted(monthly_totals.keys(), reverse=True):
        print(f"{m:<18} | {monthly_counts[m]:<8} | {monthly_totals[m]:>12.2f}")
    print("-" * 45)


def handle_sort_expenses(handler: ExpenseFileHandler) -> None:
    """Sorts expenses by amount."""
    expenses = handler.load_expenses()
    if not expenses:
        print(" No expense records found.")
        return

    print("\n1. High to Low")
    print("2. Low to High")
    choice = input("Select sort order (1-2): ").strip()
    reverse_order = choice != "2"

    sorted_exp = sorted(expenses, key=lambda e: e["Amount"], reverse=reverse_order)

    print("\n--- Sorted Expenses ---")
    print("-" * 70)
    print(f"{'Date':<12} | {'Category':<15} | {'Description':<25} | {'Amount':>8}")
    print("-" * 70)
    for exp in sorted_exp:
        print(f"{exp['Date']:<12} | {exp['Category']:<15} | {exp['Description']:<25} | {exp['Amount']:>8.2f}")
    print("-" * 70)


def handle_export_report(handler: ExpenseFileHandler) -> None:
    """Exports the summary report to a text file."""
    expenses = handler.load_expenses()
    if not expenses:
        print(" No expense records found to export.")
        return

    summary_text = generate_summary_text(expenses)
    success, msg = handler.export_summary_report(summary_text)
    print(f" {msg}")


def main() -> None:
    """Main application loop."""
    handler = ExpenseFileHandler()
    print("Welcome to Expense Tracker!")

    while True:
        display_menu()
        choice_str = input("Enter your choice (1-8): ").strip()
        if not choice_str.isdigit():
            print(" Invalid choice: Please enter a number between 1 and 8.")
            continue

        choice = int(choice_str)

        if choice == 1:
            handle_add_expense(handler)
        elif choice == 2:
            handle_view_all(handler)
        elif choice == 3:
            handle_filter_by_category(handler)
        elif choice == 4:
            handle_summary_report(handler)
        elif choice == 5:
            handle_monthly_summary(handler)
        elif choice == 6:
            handle_sort_expenses(handler)
        elif choice == 7:
            handle_export_report(handler)
        elif choice == 8:
            print("\nThank you for using Expense Tracker. Goodbye!")
            sys.exit(0)
        else:
            print(" Invalid choice: Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
