
student_records = []

while True:
    name = input("Enter student name (or 'quit' to exit): ")
    if name.lower() == 'quit':
        break

    major = input("Enter student major: ")
    age = input("Enter student age: ")

    student = {
        "name": name,
        "major": major,
        "age": age
    }
    student_records.append(student)

print("\n Student Records")
if not student_records:
    print("No records entered.")
else:
    for record in student_records:
        print(f"Name: {record['name']}, Major: {record['major']}, Age: {record['age']}")