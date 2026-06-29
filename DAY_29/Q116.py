# Inventory management system 
inventory = {}

while True:
    print("\n--- Inventory Menu ---")
    print("1. Add Item\n2. Remove Item\n3. Update Quantity\n4. Display\n5. Exit")
    
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1-5.")
        continue

    if choice == 1:
        name = input("Item name: ")
        qty = int(input("Quantity: "))
        inventory[name] = qty
    elif choice == 2:
        name = input("Item name to remove: ")
        if name in inventory:
            del inventory[name]
        else:
            print("Item not found")
    elif choice == 3:
        name = input("Item name: ")
        if name in inventory:
            qty = int(input("New quantity: "))
            inventory[name] = qty
        else:
            print("Item not found")
    elif choice == 4:
        print("\nInventory List:")
        for item, qty in inventory.items():
            print(f"{item}: {qty}")
    elif choice == 5:
        break
    else:
        print("Invalid choice")
        