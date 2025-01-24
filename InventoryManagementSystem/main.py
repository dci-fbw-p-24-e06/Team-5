from inventory.product import Product
from inventory.inventory_manager import InventoryManager


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


if __name__ == "__main__":
    main()
