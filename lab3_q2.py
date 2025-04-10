
students = []
N = int(input("Enter number of students: "))

for _ in range(N):
    name = input("Enter Name: ")
    roll_no = input("Enter Roll Number: ")
    department = input("Enter Department: ")
    address = input("Enter Address: ")
    gender = input("Enter Gender: ")
    marks = list(map(int, input("Enter Marks in 3 subjects separated by space: ").split()))

    total_marks = sum(marks)
    percentage = total_marks / 3

    student = {
        "Name": name,
        "Roll No": roll_no,
        "Department": department,
        "Address": address,
        "Gender": gender,
        "Marks": marks,
        "Total Marks": total_marks,
        "Percentage": percentage
    }
    
    students.append(student)
max_marks = max(students, key=lambda x: x['Total Marks'])
min_marks = min(students, key=lambda x: x['Total Marks'])
fail_students = [student for student in students if any(mark < 10 for mark in student["Marks"])]
for student in students:
    print("\nStudent Details:")
    for key, value in student.items():
        print(f"{key}: {value}")
    
    print(f"Total Marks: {student['Total Marks']}")
    print(f"Percentage: {student['Percentage']}%")

print(f"\nStudent with Maximum Marks: {max_marks['Name']}")
print(f"Student with Minimum Marks: {min_marks['Name']}")
print(f"Failing Students: {[student['Name'] for student in fail_students]}")
