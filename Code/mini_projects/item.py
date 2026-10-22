items = []  # store items

def add_item():
    item = input("Enter item name: ")
    items.append(item)
    print("Item added.")

def remove_item():
    item = input("Enter item name to remove: ")
    if item in items:
        items.remove(item)
        print("Item removed.")
    else:
        print("Item not found.")

def show_items():
    if not items:
        print("No items available.")
    else:
        print("Items list:")
        for i, item in enumerate(items, 1):
            print(f"{i}. {item}")

def clear_items():
    items.clear()
    print("All items cleared.")
