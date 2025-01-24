from .product import Product
from .external_service import ExternalService


class InventoryManager:
    """
    Manages a collection of products in the inventory.
    """

    def __init__(self):
        self.products = {}
        self.external_service = ExternalService()

    def add_product(self, product):
        """
        Add a product to the inventory.
        """
        self.products[product.name] = product
        self.external_service.log_product_addition(product.name)

    def remove_product(self, product_name):
        """
        Remove a product from the inventory by name.
        """
        if product_name in self.products:
            del self.products[product_name]

    def update_product_quantity(self, product_name, amount):
        """
        Update the quantity of a product.
        """
        if product_name in self.products:
            self.products[product_name].update_quantity(amount)

    def get_product_info(self, product_name):
        """
        Retrieve product information by name.
        """
        if product_name in self.products:
            return self.products[product_name].get_product_info()
        return "Product not found."

    def get_total_inventory_value(self):
        """
        Calculate the total value of all products in the inventory.
        """
        return sum(product.price * product.quantity for product in self.products.values())
