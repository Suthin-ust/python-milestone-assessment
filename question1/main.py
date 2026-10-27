student_details = [
    {"Student ID": 101, "Name": "Rahul", "Python Marks": 85, "SQL Marks": 78, "AI Marks": 90},
    {"Student ID": 102, "Name": "Anjali", "Python Marks": 72, "SQL Marks": 88, "AI Marks": 65},
    {"Student ID": 103, "Name": "Priya", "Python Marks": 70, "SQL Marks": 90, "AI Marks": 80}
]
subjects = ["Python Marks", "SQL Marks", "AI Marks"]


def get_grade(average):
    if average >= 80:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "D"


def calculate_result(s):
    marks = [s[subject] for subject in subjects]
    total = sum(marks)
    average = round(total / len(marks), 2)   # rounded to 2 decimal places
    s["Total"] = total
    s["Average"] = average
    s["Grade"] = get_grade(average)
    s["Result"] = "PASS" if average >= 40 else "FAIL"


for s in student_details:
    calculate_result(s)

print("===== Student Result =====")
for s in student_details:
    print()                                   
    print("Student ID:", s["Student ID"])
    print("Name:", s["Name"])
    print("Total:", s["Total"])
    print("Average:", s["Average"])
    print("Grade:", s["Grade"])
    print("Result:", s["Result"])


highest_score = max(student_details, key=lambda s: s["Average"])["Name"]

students_above_75 = [s["Name"] for s in student_details if s["Average"] > 75]

print()
print("Highest Scoring Student:", highest_score)
print("Students above 75:", ", ".join(students_above_75))