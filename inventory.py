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