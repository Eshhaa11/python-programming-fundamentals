inventory = []

def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            for line in file:
                name, quantity, price = line.strip().split(",")
                inventory.append({'name': name, 'quantity': quantity, 'price': price})
    except FileNotFoundError:
        
        pass

def save_inventory():
    with open("inventory.txt", "w") as file:
        for item in inventory:
            file.write(f"{item['name']},{item['quantity']},{item['price']}\n")


def add_item():
    name = input("Enter item name: ")
    quantity = input("Enter quantity: ")
    price = input("Enter price: ")
    inventory.append({'name': name, 'quantity': quantity, 'price': price})
    save_inventory()
    print(f"{name} added to inventory!")


def remove_item():
    name = input("Enter item name to remove: ")
    for item in inventory:
        if item['name'].lower() == name.lower():
            inventory.remove(item)
            save_inventory()
            print(f"{name} removed from inventory!")
            return
    print(f"{name} not found.")

def display_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Inventory List:")
        for item in inventory:
            print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}")


def search_item():
    name = input("Enter item name to search: ")
    for item in inventory:
        if item['name'].lower() == name.lower():
            print(f"Found: {item}")
            return
    print(f"{name} not found.")

def main():
    load_inventory()
    while True:
        print("\n=== Inventory Menu ===")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Display Inventory")
        print("4. Search Item")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            remove_item()
        elif choice == '3':
            display_inventory()
        elif choice == '4':
            search_item()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
