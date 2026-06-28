# Library Management System 
books=[]
issued=[]

while True:
    print("\n---Library Management System---")
    print("1.Add book")
    print("2.Display all books")
    print("3.issue book")
    print("4.return book")
    print("5.exit")

    choice=input("Enter choice:")
    if choice=="1":
        book=input("Enter book name: ")
        books.append(book)
        print(book,"added successfully")
        
    elif choice=="2":
        if len(books)==0:
            print("No books available")
        else:
            print("\nAvailable books:")
            for i in range(len(books)):
                status="(issued)" if books[i] in issued else "(Available)"
                print(i+1,".",books[i],status)

    elif choice=="3":
        book=input("Enter book name to issue:")
        if book in books and book not in issued:
            issued.append(book)
            print(book,"issued successfully.")
        elif book in issued:
            print("book is already issued.")
        else:
            print("book not found.")
    elif choice=="4":
        book=input("Enter book name to return:")
        if book in issued:
            issued.remove(book)
            print(book,"returned successfully.")
        else:
            print("this book was not issued")

    elif choice=="5":
        print("Exiting library system")
        break
    else:
        print("Invalid choice.try again")

