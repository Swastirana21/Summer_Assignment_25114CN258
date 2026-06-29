# Menu driven string 
while True:
    print("\n--- String Menu ---")
    print("1. Length\n2. Reverse\n3. Upper Case\n4. Lower Case\n5. Exit")
    choice = int(input("Enter choice: "))

    if choice == 5:
        break

    s = input("Enter a string: ")

    if choice == 1:
        print("Length:", len(s))
    elif choice == 2:
        print("Reversed:", s[::-1])
    elif choice == 3:
        print("Upper:", s.upper())
    elif choice == 4:
        print("Lower:", s.lower())
    else:
        print("Invalid choice")
        