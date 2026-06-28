# Bank Account System 
accounts=[]

while True:
    print("\n---Bank Account System---")
    print("1.Create account")
    print("2.deposit")
    print("3.withdraw")
    print("4.check balance")
    print("5.display all accounts")
    print("6.exit")

    choice=input("Enter choice:")

    if choice=="1":
        name=input("Enter account holder name:")
        balance=float(input("Enter initial deposit:"))
        accounts.append([name,balance])
        print("Account created for",name)

    elif choice=="2":
        name=input("Enter account holder name")
        found=False
        for acc in accounts:
            if acc[0]==name:
                amount=float(input("Enter deposit amount:"))
                acc[1]+=amount
                print("Deposited",amount,"|new balance:",acc[1])
                found=True
                break
        if not found:
            print("Account not found")

        elif choice=="3":
            name=input("Enter account holder name:")
            found=False
            for i in range (len(accounts)):
                if acc[i][0]==name:
                    amount=float(input("Enter withdrawl amount:"))
                    if amount<=accounts[i][1]:
                        accounts[i][1]=accounts[i][1]-amount
                        print("Withdrawn",amount,"|new balance:",acc[1])
                    else:
                        print("Insufficient balance")
                        found=True
                        break
            if not found:
                print("Account not found")
        
        elif choice=="4":
            name=input("Enter account holder name")
            found=False
            for acc in accounts:
                if acc[0]==name:
                    print("balance for",name,":",acc[1])
                    found=True
                    break
                if not found:
                    print("Account not found")
        elif choice=="5":
            if len(accounts)==0:
                print("No accounts found")
            else:
                print("\nAll accounts:")
                for acc in accounts:
                    print("Name:",acc[0],"|balance:",acc[1])

        elif choice=="6":
            print("Exiting bank system")
            break
        else:
            print("invalid choice. try again")


            