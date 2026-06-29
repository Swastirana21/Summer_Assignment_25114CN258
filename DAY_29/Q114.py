# Menu-driven array operation system 
arr = []

while True:
    print("\n--- Array Menu ---")
    print("1. Insert\n2. Delete\n3. Display\n4. Search\n5. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        val = int(input("Enter value to insert: "))
        arr.append(val)
    elif choice == 2:
        val = int(input("Enter value to delete: "))
        if val in arr:
            arr.remove(val)
        else:
            print("Value not found")
    elif choice == 3:
        print("Array:", arr)
    elif choice == 4:
        val = int(input("Enter value to search: "))
        print("Found" if val in arr else "Not found")
    elif choice == 5:
        break
    else:
        print("Invalid choice")
        