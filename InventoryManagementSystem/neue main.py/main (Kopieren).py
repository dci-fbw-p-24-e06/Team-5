from inventory.product import Product
from inventory.inventory_manager import InventoryManager

def print_menu():
    """Display the terminal menu.
    """
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Change Item")
    print("4. Summary")
    print("5. Exit")

def add_item(inventory):
    """
    Add a new item to the inventory.
    """
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    
    # Create a new product and add it to the inventory
    product = Product(name, price, quantity)
    inventory.add_product(product)
    print(f"{name} has been added to the inventory.")

def remove_item(inventory):
    """
    Remove an item from the inventory.
    """
    name = input("Enter the product name to remove: ")
    if name in inventory.products:
        inventory.remove_product(name)
        print(f"{name} has been removed from the inventory.")
    else:
        print(f"Product {name} not found in the inventory.")

def change_item(inventory):
    """
    Change the details (price, quantity) of an item in the inventory.
    """
    name = input("Enter the product name to change: ")
    if name in inventory.products:
        new_price = float(input(f"Enter new price for {name}: "))
        new_quantity = int(input(f"Enter new quantity for {name}: "))
        
        # Update product details
        product = inventory.products[name]
        product.price = new_price
        product.quantity = new_quantity
        print(f"{name} has been updated with new price and quantity.")
    else:
        print(f"Product {name} not found in the inventory.")

def summary(inventory):
    """
    Display a summary of the current inventory.
    """
    if not inventory.products:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for product_name in inventory.products.keys():
            print(inventory.get_product_info(product_name))
        total_value = inventory.get_total_inventory_value()
        print(f"Total inventory value: ${total_value:,.2f}")

def main():
    """
    Main entry point for the Inventory Management System.
    """
    inventory = InventoryManager()

    # Add some quirky products
    inventory.add_product(Product("Laptop", 1500, 5))
    inventory.add_product(Product("Smartphone", 800, 10))
    inventory.add_product(Product("Banana Phone", 25, 100))  # Call your friends in style!
    inventory.add_product(Product("Invisible Cloak", 9999, 2))  # Harry Potter's favorite
    inventory.add_product(Product("Self-Folding Laundry", 1200, 3))  # Because we all need this
    inventory.add_product(Product("Rocket-Powered Roller Skates", 5000, 1))  # Straight out of cartoons
    inventory.add_product(Product("Unicorn Horn (Replica)", 250, 50))  # Ethical magic!
    inventory.add_product(Product("Cat Translator", 150, 20))  # Because "meow" isn't enough
    inventory.add_product(Product("Anti-Gravity Boots", 2000, 4))  # Walk on walls like a boss
    inventory.add_product(Product("Time Machine (Model T-1000)", 500000, 1))  # For the adventurous

    # Display product information
    for product_name in inventory.products.keys():
        print(inventory.get_product_info(product_name))

    # Display total inventory value
    print(f"Total inventory value: ${inventory.get_total_inventory_value():,.2f}")


    while True:
        print_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            remove_item(inventory)
        elif choice == "3":
            change_item(inventory)
        elif choice == "4":
            summary(inventory)
        elif choice == "5":
            print("Exiting the program.")
            break  # Exit the program
        else:
            print("Invalid choice. Please choose a valid option (1-5).")

if __name__ == "__main__":
    main()
