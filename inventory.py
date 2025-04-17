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