# Student Management System in Core Python

students = []  # List to store student records

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    student = {
        "roll": roll,
        "name": name,
        "marks": marks
    }
    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students found!\n")
        return

    print("\n--- Student List ---")
    for s in students:
        print(f"Roll: {s['roll']} | Name: {s['name']} | Marks: {s['marks']}")
    print()

def search_student():
    roll = input("Enter Roll Number to Search: ")
    for s in students:
        if s["roll"] == roll:
            print(f"\nStudent Found:")
            print(f"Roll: {s['roll']} | Name: {s['name']} | Marks: {s['marks']}\n")
            return
    print("Student not found!\n")

def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully!\n")
            return
    print("Student not found!\n")

while True:
    print("------ Student Management System ------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.\n")
