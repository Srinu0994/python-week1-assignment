"""
models.py
---------
Contains data models and management logic for the Student Management System.
Demonstrates Object-Oriented Programming (OOP) concepts: Encapsulation, Methods, and Data Persistence.
"""

import json
import os
from typing import List, Dict, Optional, Any


class Student:
    """
    Represents an individual student entity.
    """

    def __init__(self, student_id: str, name: str, age: int, course: str, marks: float):
        self.student_id = str(student_id).strip()
        self.name = name.strip()
        self.age = int(age)
        self.course = course.strip()
        self.marks = float(marks)

    def to_dict(self) -> Dict[str, Any]:
        """Convert student object to a dictionary for JSON serialization."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Student":
        """Create a Student instance from a dictionary."""
        return cls(
            student_id=data["student_id"],
            name=data["name"],
            age=data["age"],
            course=data["course"],
            marks=data["marks"],
        )

    def __str__(self) -> str:
        """Formatted string representation of the student."""
        return (
            f"ID: {self.student_id:<6} | Name: {self.name:<15} | "
            f"Age: {self.age:<3} | Course: {self.course:<12} | Marks: {self.marks:>5.1f}"
        )


class StudentManager:
    """
    Manages a collection of Student objects, providing CRUD operations,
    sorting, analytics, and JSON file persistence.
    """

    def __init__(self, storage_path: str = "students.json"):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.storage_path = os.path.join(base_dir, storage_path)
        self.students: Dict[str, Student] = {}
        self.load_from_json()

    def add_student(self, student: Student) -> tuple[bool, str]:
        """
        Add a new student. Enforces unique student_id.
        """
        if student.student_id in self.students:
            return False, f"Error: Student ID '{student.student_id}' already exists."

        self.students[student.student_id] = student
        self.save_to_json()
        return True, f"Success: Student '{student.name}' (ID: {student.student_id}) added successfully."

    def get_all_students(self) -> List[Student]:
        """Return a list of all students."""
        return list(self.students.values())

    def search_student(self, query: str) -> List[Student]:
        """
        Search students by ID or Name (case-insensitive search).
        """
        query_str = query.strip().lower()
        results = []
        for student in self.students.values():
            if (
                query_str == student.student_id.lower()
                or query_str in student.name.lower()
            ):
                results.append(student)
        return results

    def get_student_by_id(self, student_id: str) -> Optional[Student]:
        """Retrieve a single student by exact ID."""
        return self.students.get(str(student_id).strip())

    def update_student(
        self,
        student_id: str,
        name: Optional[str] = None,
        age: Optional[int] = None,
        course: Optional[str] = None,
        marks: Optional[float] = None,
    ) -> tuple[bool, str]:
        """
        Update attributes of an existing student.
        """
        student = self.get_student_by_id(student_id)
        if not student:
            return False, f"Error: No student found with ID '{student_id}'."

        if name is not None and name.strip():
            student.name = name.strip()
        if age is not None:
            student.age = int(age)
        if course is not None and course.strip():
            student.course = course.strip()
        if marks is not None:
            student.marks = float(marks)

        self.save_to_json()
        return True, f"Success: Student ID '{student_id}' updated successfully."

    def delete_student(self, student_id: str) -> tuple[bool, str]:
        """
        Delete a student by ID.
        """
        student_id_str = str(student_id).strip()
        if student_id_str not in self.students:
            return False, f"Error: No student found with ID '{student_id_str}'."

        removed_student = self.students.pop(student_id_str)
        self.save_to_json()
        return True, f"Success: Student '{removed_student.name}' (ID: {student_id_str}) deleted successfully."

    def sort_students(self, by: str = "marks", reverse: bool = True) -> List[Student]:
        """
        Sort students by 'marks' or 'name'.
        """
        students_list = self.get_all_students()
        if by == "marks":
            return sorted(students_list, key=lambda s: s.marks, reverse=reverse)
        elif by == "name":
            return sorted(students_list, key=lambda s: s.name.lower(), reverse=reverse)
        elif by == "id":
            return sorted(students_list, key=lambda s: s.student_id)
        return students_list

    def calculate_average_marks(self) -> float:
        """Calculate and return the class average marks."""
        if not self.students:
            return 0.0
        total_marks = sum(s.marks for s in self.students.values())
        return total_marks / len(self.students)

    def get_top_performer(self) -> Optional[Student]:
        """Find and return the student with the highest marks."""
        if not self.students:
            return None
        return max(self.students.values(), key=lambda s: s.marks)

    def save_to_json(self) -> None:
        """Save all student records to JSON file."""
        try:
            data = [s.to_dict() for s in self.students.values()]
            with open(self.storage_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            print(f"Error saving to JSON file: {e}")

    def load_from_json(self) -> None:
        """Load student records from JSON file if present."""
        if not os.path.exists(self.storage_path):
            self.students = {}
            return

        try:
            with open(self.storage_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.students = {
                    item["student_id"]: Student.from_dict(item) for item in data
                }
        except (json.JSONDecodeError, IOError, KeyError) as e:
            print(f"Warning: Failed to load data from {self.storage_path}: {e}")
            self.students = {}
