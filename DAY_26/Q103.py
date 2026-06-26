# ATM simulation 
def atm_simulation():
    balance=5000
    print("Welcome to Atm")
    print("1.Check Balance")
    print("2.Withdrawl")
    print("3.Deposit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("Your balance is:",balance)
    elif choice==2:
        amount=int(input("Enter amount to withdrawl:"))
        if amount<=balance:
            balance-=amount
            print("Withdrawal successful! New balance:",balance)
        else:
            print("Invalid choice")
atm_simulation()
