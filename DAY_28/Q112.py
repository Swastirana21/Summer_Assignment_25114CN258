# Contact management system 
contacts=[]
while True:
    print("\n---Contact Management System---")
    print("1.Add contact")
    print("2.Search Contact")
    print("3.Update contract")
    print("4.Delete contact")
    print("5.Display all contacts")
    print("6.Exit")

    choice=input("enter choice:")
    if choice=="1":
        name=input("Enter name:")
        phone=input("enter phone number:")
        contacts.append([name,phone])
        print("contact added:",name)

    elif choice=="2":
        name=input("Enter name to search:")
        found=False
        for c in contacts:
            if c[0]==name:
                print("Name:",c[0],"|Phone:",c[1])
                found=True
                break
        if not found:
            print("Contact not found")

    elif choice=="3":
        name=input("Enter name to update:")
        found=False
        for c in contacts:
            if c[0]==name:
                new_phone=input("Enter new phone number:")
                c[1]=new_phone
                print("Contact updated for",name)
                found=True
                break
        if not found:
            print("Contact not found")

    elif choice=="4":
        name=input("Enter name to delete")
        found=False
        for c in contacts:
            if c[0]==name:
                contacts.remove(c)
                print("contacts deleted:",name)
                found=True
                break
        if not found:
            print("Contact not found")

    elif choice=="5":
        if len(contacts)==0:
            print("No contacts saved")
        else:
            print("\n All contacts:")
            for c in contacts:
                print("Name:",c[0],"|phone:",c[1])

    elif choice=="6":
        print("Exiting contact management system")
        break
    else:
        print("Invalid choice.Try again")
        