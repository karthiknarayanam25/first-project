students = []

while True:
    print("\n--- STUDENT ENTRY ---")
    name = input("Enter student name (or type 'stop'): ")
    if name.lower() == "stop":
        break
    maths = int(input("Maths marks: "))
    science = int(input("Science marks: "))
    english = int(input("English marks: "))
    total = maths + science + english
    percentage = total / 3
    if percentage >= 80:
        grade = "A+"
    elif percentage >= 60:
        grade = "A"
    elif percentage >= 40:
        grade = "B"
    else:
        grade = "C"
    if percentage >= 35:
        result = "PASS"
    else:
        result = "FAIL"
    student = {
        "name": name,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "result": result
    }
    students.append(student)
print("\n\n===== FINAL REPORT =====")
for s in students:
    print("\nName:", s["name"])
    print("Total:", s["total"])
    print("Percentage:", s["percentage"])
    print("Grade:", s["grade"])
    print("Result:", s["result"])
print("\nTotal Students:", len(students))