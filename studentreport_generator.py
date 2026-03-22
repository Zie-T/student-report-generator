students = {}
number = int(input("How many students are in class?: "))

for i in range(number):
    name = input("Enter the student's name: ")
    while True:
            try:
                mark = int(input("Enter the student's mark: "))
                break
        
            except ValueError:
                print("Invalid mark! Please enter a number between 0 and 100")
    
    students[name] = mark
    
    
print("=" * 30)
print("  STUDENT REPORT CARD")
print("=" * 30)
marks = list(students.values())
average = sum(marks) / len(marks)
students_passed = 0
students_failed = 0
for name, mark in students.items():
    if mark >= 50:
        students_passed += 1
        print(f"{name} - Passed✅")
    else:
        students_failed += 1
        print(f"{name} - Failed❌")

top_student = max(students, key =lambda value: students[value])


print("=" * 30)
print(f"Class Average: {average: .2f}%")
print(f"Top Student: {top_student} with {students[top_student]}%")
print(f"Students Passed: {students_passed}")
print(f"Students Failed: {students_failed}")
print("=" * 30)

with open("student_report.txt", "w", encoding="utf-8") as file:
    file.write("=" * 30 + "\n")
    file.write("  STUDENT REPORT CARD\n")
    file.write("=" * 30 + "\n")

    for name, mark in students.items():
        if mark >= 50:

            file.write(f"{name} - Passed✅\n")
        else:
            file.write(f"{name} - Failed❌\n")
    

    file.write("=" * 30 + "\n")
    file.write(f"Class Average: {average: .2f}%\n")
    file.write(f"Top Student: {top_student} with {students[top_student]}%\n")
    file.write(f"Students Passed: {students_passed}\n")
    file.write(f"Students Failed: {students_failed}\n")
    file.write("=" * 30 + "\n")


with open("student_report.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)








