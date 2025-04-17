inventory = []

def add_item():
    name = input("Enter an item name: ")
    quantity = input("Enter the quanity: ")
    price = input("Enter price: ")

    item = {
        'name': name,
        'quantity': quantity,
        'price': price
    }

    inventory.append(item)
    print(f"{name} has been added to inventory.\n")

def remove_item() :
    name = input("Enter the the item to remove: ")
    found = False
    for item in inventory:
        if item['name'].lower() == name.lower():
            inventory.remove(item)
            print(f"{name} has been removed from inventory.\n")
            found = True
            break
    if not found:
        print(f"{name} not found in inventory.\n")

def display_inventory():
    if not inventory:
        print("Inventory is empty.\n")
        return
    print("Current Inventory:")
    for item in inventory:
        print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}")
    print()

def search_item():
    name = input("Enter the name of the item to search: ")
    found = False
    for item in inventory:
        if item['name'].lower() == name.lower():
            print(f"Found: Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}\n")
            found = True
            break
    if not found:
        print(f"{name} not found in inventory.\n")

def main():
    while True:
        print("=== Inventory Management System ===")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Display Inventory")
        print("4. Search Item")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            remove_item()
        elif choice == '3':
            display_inventory()
        elif choice == '4':
            search_item()
        elif choice == '5':
            print("Exiting Inventory Management System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.\n")