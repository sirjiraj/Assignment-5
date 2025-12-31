student_marks = {
    "Ankit": 85,
    "Bablu": 92,
    "Chanchal": 78,
    "Divyansh": 95,
    "Mohit":56  }

name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")
