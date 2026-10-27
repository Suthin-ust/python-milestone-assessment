# Simple Employee File Management

## Problem Statement

Develop a small Python application that maintains employee information. Employee details are stored in a file and later read to generate a simple report:

- Create a file called `employees.txt`
- Store Employee ID, Name, Role and Salary
- Read the employee information from the file
- Display all employees
- Show employees whose salary is greater than ₹50,000
- Find the employee with the highest salary
- Count how many employees belong to each role
- Handle the case where the file does not exist

## Approach / Logic Used

1. Create an **`Employee` class** with `employee_id`, `name`, `role` and `salary`, and a `display_details()` method to print them.
2. `create_file()` creates an empty `employees.txt`, so running the program again does not add the same records twice.
3. `add_employee()` appends one employee to the file as a comma-separated line.
4. `read_employees()` opens the file, splits each line on commas and creates an `Employee` object for it. If the file is missing, it catches `FileNotFoundError` and prints an error message instead of crashing.
5. Display every employee using `display_details()` in a `for` loop.
6. Find employees with a salary **above ₹50,000** using a list comprehension.
7. `find_highest_salary()` uses `max()` to find the highest-paid employee.
8. `find_employees_by_role()` groups employees into a dictionary by role. The count for each role is the length of its list.

All file operations use a **context manager** (`with open()`), so the file is closed automatically.

## How to Run

1. Install Python 3.
2. Open a terminal in the project folder.
3. Run:
   ```bash
   python question2.py
   ```
   On Windows, if `python` is not recognised, use `py question2.py`.

The program creates `employees.txt` automatically.

## Sample Input

Contents of `employees.txt` (Employee ID, Name, Role, Salary):

```
101,Rahul,Python Developer,50000
102,Anjali,Tester,45000
103,John,Developer,60000
104,Priya,Tester,48000
```

## Sample Output

```
===== Employee Details =====

101 - Rahul - Python Developer - ₹50000
102 - Anjali - Tester - ₹45000
103 - John - Developer - ₹60000
104 - Priya - Tester - ₹48000

===== Employees with Salary > 50000 =====

John - ₹60000

Highest Paid Employee:
John - ₹60000

Employee Count by Role:
Developer: 1
Python Developer: 1
Tester: 2
```

If `employees.txt` does not exist when it is read:

```
Error: employees.txt does not exist.
```

## Python Concepts Used

| Concept | Where it is used |
|---|---|
| Class and Object | `Employee` class with `__init__()` |
| Method | `display_details()` |
| Functions | `create_file()`, `add_employee()`, `read_employees()`, `find_highest_salary()`, `find_employees_by_role()` |
| File Handling | Writing (`"w"`), appending (`"a"`) and reading (`"r"`) `employees.txt` |
| Context Manager | `with open()` for every file operation |
| Exception Handling | `try/except FileNotFoundError` |
| Lists | List of `Employee` objects |
| Dictionaries | Grouping employees by role |
| Loops | Reading lines, displaying employees, printing role counts |
| Conditional Statements | Salary check, empty line check, role check |
| List Comprehension | Employees with salary above ₹50,000 |
| Built-in Functions | `max()`, `len()`, `sorted()`, `int()` |
| String Methods | `strip()`, `split()`, f-strings |