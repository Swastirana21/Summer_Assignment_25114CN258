# Student record system 
students = []

while True:
    print("\n--- Student Record Menu ---")
    print("1. Add Student\n2. Display All\n3. Search Student\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students.append({"name": name, "marks": marks})
    elif choice == 2:
        print("\nStudent List:")
        for s in students:
            print(f"Name: {s['name']}, Marks: {s['marks']}")
    elif choice == 3:
        name = input("Enter name to search: ")
        found = False
        for s in students:
            if s["name"].lower() == name.lower():
                print(f"Found: {s['name']} - Marks: {s['marks']}")
                found = True
                break
        if not found:
            print("Student not found")
    elif choice == 4:
        break
    else:
        print("Invalid choice")
        