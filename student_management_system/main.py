"""
main.py
-------
Console entry point for the Student Management System.
Provides a interactive, menu-driven CLI interface for full CRUD operations and student analytics.
"""

import sys
from models import Student, StudentManager
from utils import (
    get_valid_int,
    get_valid_float,
    get_non_empty_string,
    get_yes_no,
)


def display_menu() -> None:
    """Displays the main menu options."""
    print("\n" + "=" * 40)
    print("  ===== Student Management System =====")
    print("=" * 40)
    print("  1. Add Student")
    print("  2. View All Students")
    print("  3. Search Student (by ID or Name)")
    print("  4. Update Student")
    print("  5. Delete Student")
    print("  6. Sort Students (by Marks / Name)")
    print("  7. Class Analytics (Average & Top Performer)")
    print("  8. Exit")
    print("=" * 40)


def handle_add_student(manager: StudentManager) -> None:
    """Handles adding a new student record."""
    print("\n--- Add New Student ---")
    student_id = get_non_empty_string("Enter Student ID: ")
    if manager.get_student_by_id(student_id):
        print(f" Error: Student ID '{student_id}' already exists!")
        return

    name = get_non_empty_string("Enter Full Name: ")
    age = get_valid_int("Enter Age (5 to 100): ", min_val=5, max_val=100)
    course = get_non_empty_string("Enter Course Name: ")
    marks = get_valid_float("Enter Marks (0 to 100): ", min_val=0.0, max_val=100.0)

    student = Student(student_id, name, age, course, marks)
    success, message = manager.add_student(student)
    print(f" {message}")


def handle_view_students(manager: StudentManager) -> None:
    """Handles viewing all stored student records."""
    print("\n--- Student Records ---")
    students = manager.get_all_students()
    if not students:
        print(" No student records found.")
        return

    print("-" * 75)
    for student in students:
        print(student)
    print("-" * 75)
    print(f" Total Students: {len(students)}")


def handle_search_student(manager: StudentManager) -> None:
    """Handles searching for a student by ID or Name."""
    print("\n--- Search Student ---")
    query = get_non_empty_string("Enter Student ID or Name to search: ")
    results = manager.search_student(query)

    if not results:
        print(f" No student found matching query: '{query}'")
        return

    print(f"\n Search Results ({len(results)} found):")
    print("-" * 75)
    for student in results:
        print(student)
    print("-" * 75)


def handle_update_student(manager: StudentManager) -> None:
    """Handles updating existing student information."""
    print("\n--- Update Student ---")
    student_id = get_non_empty_string("Enter Student ID to update: ")
    student = manager.get_student_by_id(student_id)

    if not student:
        print(f" Error: Student ID '{student_id}' not found.")
        return

    print(f"Current Record: {student}")
    print("\nLeave input blank to keep current value:")

    new_name = get_non_empty_string("Enter New Name: ", allow_empty=True)
    new_age = get_valid_int(
        "Enter New Age (5-100): ", min_val=5, max_val=100, allow_empty=True
    )
    new_course = get_non_empty_string("Enter New Course: ", allow_empty=True)
    new_marks = get_valid_float(
        "Enter New Marks (0-100): ", min_val=0.0, max_val=100.0, allow_empty=True
    )

    success, message = manager.update_student(
        student_id=student_id,
        name=new_name,
        age=new_age,
        course=new_course,
        marks=new_marks,
    )
    print(f" {message}")


def handle_delete_student(manager: StudentManager) -> None:
    """Handles deleting a student record with confirmation."""
    print("\n--- Delete Student ---")
    student_id = get_non_empty_string("Enter Student ID to delete: ")
    student = manager.get_student_by_id(student_id)

    if not student:
        print(f" Error: Student ID '{student_id}' not found.")
        return

    print(f"Found Record: {student}")
    confirm = get_yes_no(
        f"Are you sure you want to delete student '{student.name}'?"
    )
    if confirm:
        success, message = manager.delete_student(student_id)
        print(f" {message}")
    else:
        print(" Deletion cancelled.")


def handle_sort_students(manager: StudentManager) -> None:
    """Handles sorting student records by marks or name."""
    print("\n--- Sort Students ---")
    print("1. Sort by Marks (Descending)")
    print("2. Sort by Marks (Ascending)")
    print("3. Sort by Name (Alphabetical)")
    choice = get_valid_int("Enter sorting choice (1-3): ", min_val=1, max_val=3)

    if choice == 1:
        sorted_list = manager.sort_students(by="marks", reverse=True)
    elif choice == 2:
        sorted_list = manager.sort_students(by="marks", reverse=False)
    else:
        sorted_list = manager.sort_students(by="name", reverse=False)

    print("\nSorted Records:")
    print("-" * 75)
    for s in sorted_list:
        print(s)
    print("-" * 75)


def handle_analytics(manager: StudentManager) -> None:
    """Displays class average and top performing student."""
    print("\n--- Class Analytics ---")
    students = manager.get_all_students()
    if not students:
        print(" No student records available for analytics.")
        return

    avg_marks = manager.calculate_average_marks()
    top_student = manager.get_top_performer()

    print(f" Total Enrolled Students : {len(students)}")
    print(f" Class Average Marks    : {avg_marks:.2f}")
    if top_student:
        print(f" Top Performing Student : {top_student.name} (ID: {top_student.student_id}) with {top_student.marks:.1f} marks")


def main() -> None:
    """Main execution loop."""
    manager = StudentManager()
    print("Welcome to Student Management System!")

    while True:
        display_menu()
        choice = get_valid_int("Enter your choice (1-8): ", min_val=1, max_val=8)

        if choice == 1:
            handle_add_student(manager)
        elif choice == 2:
            handle_view_students(manager)
        elif choice == 3:
            handle_search_student(manager)
        elif choice == 4:
            handle_update_student(manager)
        elif choice == 5:
            handle_delete_student(manager)
        elif choice == 6:
            handle_sort_students(manager)
        elif choice == 7:
            handle_analytics(manager)
        elif choice == 8:
            print("\nThank you for using Student Management System. Goodbye!")
            sys.exit(0)


if __name__ == "__main__":
    main()
