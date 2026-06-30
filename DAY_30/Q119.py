# Mini employee management system 
employees = []

while True:
    print("\n--- Employee Menu ---")
    print("1. Add Employee\n2. Display All\n3. Update Salary\n4. Remove Employee\n5. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter employee name: ")
        salary = float(input("Enter salary: "))
        employees.append({"name": name, "salary": salary})
    elif choice == 2:
        print("\nEmployee List:")
        for emp in employees:
            print(f"Name: {emp['name']}, Salary: {emp['salary']}")
    elif choice == 3:
        name = input("Enter name to update: ")
        for emp in employees:
            if emp["name"].lower() == name.lower():
                emp["salary"] = float(input("Enter new salary: "))
                print("Salary updated")
                break
        else:
            print("Employee not found")
    elif choice == 4:
        name = input("Enter name to remove: ")
        for emp in employees:
            if emp["name"].lower() == name.lower():
                employees.remove(emp)
                print("Employee removed")
                break
        else:
            print("Employee not found")
    elif choice == 5:
        break
    else:
        print("Invalid choice")
        