# Student Management System

A robust, menu-driven Python console application for managing student records using Object-Oriented Programming (OOP) principles and persistent JSON storage.

## Objective
To provide an interactive CLI tool allowing administrators to perform full CRUD operations (Create, Read, Update, Delete), sorting, and performance analytics on student data with zero crashes and strict input validation.

## Features
- **Full CRUD Operations**:
  - **Add Student**: Enforces unique student IDs, age (5-100), and marks (0-100).
  - **View Students**: Displays neatly formatted student tables.
  - **Search Student**: Query by ID or case-insensitive student name.
  - **Update Student**: Modify fields selectively while keeping existing values.
  - **Delete Student**: Deletes student records with an explicit safety confirmation prompt.
- **Advanced Features**:
  - **Persistent JSON Storage**: Records automatically persist across restarts in `students.json`.
  - **Sorting**: Sort records by Marks (ascending/descending) or Name.
  - **Analytics**: Calculates class average marks and identifies the top-performing student.
- **Error Handling**: Gracefully handles non-numeric inputs, duplicate IDs, and invalid choices without tracebacks.

## Technologies Used
- Python 3.10+
- Built-in `json`, `os`, `sys`, and `typing` modules

## Project Structure
```text
student_management_system/
├── main.py        # Interactive CLI menu & workflow handler
├── models.py      # Student & StudentManager OOP classes with JSON storage logic
├── utils.py       # Helper functions for robust user input validation
├── students.json  # Data persistence file (auto-generated)
└── README.md      # Project documentation
```

## How to Run
From the repository root or directory, run:
```bash
python student_management_system/main.py
```

## Sample Input and Output

### Sample Run 1: Adding a Student & Viewing Records
```text
===== Student Management System =====
1. Add Student
2. View All Students
...
Enter your choice (1-8): 1

--- Add New Student ---
Enter Student ID: 101
Enter Full Name: Neha Sharma
Enter Age (5 to 100): 20
Enter Course Name: Python
Enter Marks (0 to 100): 91.5
 Success: Student 'Neha Sharma' (ID: 101) added successfully.

Enter your choice (1-8): 2

--- Student Records ---
---------------------------------------------------------------------------
ID: 101    | Name: Neha Sharma     | Age: 20  | Course: Python       | Marks:  91.5
---------------------------------------------------------------------------
 Total Students: 1
```

### Sample Run 2: Analytics & Top Performer
```text
Enter your choice (1-8): 7

--- Class Analytics ---
 Total Enrolled Students : 3
 Class Average Marks    : 87.50
 Top Performing Student : Neha Sharma (ID: 101) with 91.5 marks
```

## Author
- **Author**: [Your Name]
- **Role**: Python Developer Intern (WeIntern Pvt Ltd)
