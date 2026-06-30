# Mini library system 
library = []

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book\n2. Issue Book\n3. Return Book\n4. Display Books\n5. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        title = input("Enter book title: ")
        library.append({"title": title, "issued": False})
    elif choice == 2:
        title = input("Enter book title to issue: ")
        for book in library:
            if book["title"].lower() == title.lower() and not book["issued"]:
                book["issued"] = True
                print("Book issued successfully")
                break
        else:
            print("Book not available")
    elif choice == 3:
        title = input("Enter book title to return: ")
        for book in library:
            if book["title"].lower() == title.lower() and book["issued"]:
                book["issued"] = False
                print("Book returned successfully")
                break
        else:
            print("Invalid return request")
    elif choice == 4:
        print("\nLibrary Books:")
        for book in library:
            status = "Issued" if book["issued"] else "Available"
            print(f"{book['title']} - {status}")
    elif choice == 5:
        break
    else:
        print("Invalid choice")
        