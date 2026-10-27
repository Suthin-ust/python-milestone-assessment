FILE_NAME = "employees.txt"


class Employee:
	def __init__(self, employee_id, name, role, salary):
		self.employee_id = employee_id
		self.name = name
		self.role = role
		self.salary = salary

	def display_details(self):
		print(f"{self.employee_id} - {self.name} - {self.role} - ₹{self.salary}")


def create_file():
	with open(FILE_NAME, "w", encoding="utf-8"):
		pass


def add_employee(employee_id, name, role, salary):
	with open(FILE_NAME, "a", encoding="utf-8") as file:
		file.write(f"{employee_id},{name},{role},{salary}\n")

def read_employees():
	employees = []
	try:
		with open(FILE_NAME, "r", encoding="utf-8") as file:
			for line in file:
				line = line.strip()
				if line:
					employee_id, name, role, salary = line.split(",")
					employees.append(Employee(int(employee_id), name, role, int(salary)))
	except FileNotFoundError:
		print(f"Error: {FILE_NAME} does not exist.")
	return employees


def find_highest_salary(employees):
	return max(employees, key=lambda e: e.salary)


def find_employees_by_role(employees):
	roles = {}
	for e in employees:
		if e.role not in roles:
			roles[e.role] = []
		roles[e.role].append(e)
	return roles


create_file()
add_employee(101, "Rahul", "Python Developer", 50000)
add_employee(102, "Anjali", "Tester", 45000)
add_employee(103, "John", "Developer", 60000)
add_employee(104, "Priya", "Tester", 48000)

employees = read_employees()

if employees:
	print("===== Employee Details =====")
	print()
	for e in employees:
		e.display_details()


	high_salary = [e for e in employees if e.salary > 50000]
	print()
	print("===== Employees with Salary > 50000 =====")
	print()
	for e in high_salary:
		print(f"{e.name} - ₹{e.salary}")

	highest = find_highest_salary(employees)
	print()
	print("Highest Paid Employee:")
	print(f"{highest.name} - ₹{highest.salary}")

	roles = find_employees_by_role(employees)
	print()
	print("Employee Count by Role:")
	for role in sorted(roles):
		print(f"{role}: {len(roles[role])}")
else:
	print("No employee records found.")
