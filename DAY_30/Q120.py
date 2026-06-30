# MINI PROJECT
# Student Management System using Functions

students = []

def add_student():
    name = input("Enter student name: ")
    roll = int(input("Enter roll number: "))
    marks = list(map(int, input("Enter marks (space separated): ").split()))
    students.append({"name": name, "roll": roll, "marks": marks})
    print("Student added successfully!")

def display_students():
    if not students:
        print("No records found.")
        return
    print("\n--- Student List ---")
    for s in students:
        avg = calculate_average(s["marks"])
        print(f"Roll: {s['roll']}, Name: {s['name']}, Avg Marks: {avg:.2f}")

def calculate_average(marks):
    return sum(marks) / len(marks)

def search_student():
    roll = int(input("Enter roll number to search: "))
    for s in students:
        if s["roll"] == roll:
            avg = calculate_average(s["marks"])
            print(f"Found -> Name: {s['name']}, Avg Marks: {avg:.2f}")
            return
    print("Student not found.")

def find_topper():
    if not students:
        print("No records found.")
        return
    topper = max(students, key=lambda s: calculate_average(s["marks"]))
    print(f"Topper: {topper['name']} with Avg Marks: {calculate_average(topper['marks']):.2f}")

def main():
    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student\n2. Display All\n3. Search Student\n4. Find Topper\n5. Exit")
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input. Please enter a number (1-5).")
            continue

        if choice == 1:
            add_student()
        elif choice == 2:
            display_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            find_topper()
        elif choice == 5:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

main()
