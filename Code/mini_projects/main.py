from login import login_system
import item

# --- login first ---
if not login_system():
    exit()

# --- main menu ---
while True:
    print("\n--- Item Management Menu ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. Show items")
    print("4. Clear items")
    print("5. Exit")

    choice = input("Choose option: ")

    match choice:
        case "1":
            item.add_item()
        case "2":
            item.remove_item()
        case "3":
            item.show_items()
        case "4":
            item.clear_items()
        case "5":
            print("Goodbye!")
            break
        case _:
            print("Invalid option.")
