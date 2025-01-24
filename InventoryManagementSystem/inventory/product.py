class Product:
    """
    Represents a product in the inventory.
    """

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount):
        """
        Update the quantity of the product.
        """
        self.quantity += amount

    def update_price(self, new_price):
        """
        Update the price of the product.
        """
        self.price = new_price

    def get_product_info(self):
        """
        Return a string representation of the product's information.
        """
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
