# Ticket Booking System 
tickets=[]
total_seats=10
booked_seats=[]

while True:
    print("\n---Ticket Booking System---")
    print("1.Book ticket")
    print("2.Cancel ticket")
    print("3.View all bookings")
    print("4.Check available seats")
    print("5.Exit")

    choice=input("Enter choice:")
    if choice =="1":
        if len(booked_seats)==total_seats:
            print("Sorry, all seats are booked")
        else:
            name=input("Enter passenger name:")
            seat=1
            while seat in booked_seats:
                seat+=1
            tickets.append([name,seat])
            booked_seats.append(seat)
            print("Ticket booked for",name,"|seat no:",seat)
    elif choice=="2":
        name=input("Enter passenger name to cancel:")
        found=False
        for t in tickets:
            if t[0]==name:
                booked_seats.remove(t[1])
                tickets.remove(t)
                print("Tickets cancelled for",name)
                found=True
                break
        if not found:
            print("Booking not found")
    elif choice=="3":
        if len(tickets)==0:
            print("\nNo bookings yet")
        else:
            print("\nAll bookings:")
            for t in tickets:
                print("Passenger:",t[0],"|Seat:",t[1])

    elif choice=="4":
        available=total_seats-len(booked_seats)
        print("Available Seats:",available,"/",total_seats)

    elif choice=="5":
        print("Exiting ticket booking system")
        break
    else:
        print("Invalid choice.try again")
