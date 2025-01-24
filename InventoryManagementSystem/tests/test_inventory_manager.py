import unittest
from inventory.product import Product
from inventory.inventory_manager import InventoryManager


class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        """
        Setup an InventoryManager instance before each test.
        """
        self.inventory = InventoryManager()
        self.product = Product("Tablet", 500, 20)
        self.inventory.add_product(self.product)

    def test_add_product(self):
        """
        Test adding a product to the inventory.
        """
        self.assertIn("Tablet", self.inventory.products)

    def test_remove_product(self):
        """
        Test removing a product from the inventory.
        """
        self.inventory.remove_product("Tablet")
        self.assertNotIn("Tablet", self.inventory.products)

    def test_update_product_quantity(self):
        """
        Test updating the quantity of a product.
        """
        self.inventory.update_product_quantity("Tablet", 10)
        self.assertEqual(self.inventory.products["Tablet"].quantity, 30)

    def test_get_product_info(self):
        """
        Test retrieving product information.
        """
        self.assertEqual(
            self.inventory.get_product_info("Tablet"),
            "Product: Tablet, Price: 500, Quantity: 20"
        )

    def test_get_total_inventory_value(self):
        """
        Test calculating the total inventory value.
        """
        self.assertEqual(self.inventory.get_total_inventory_value(), 10000)


if __name__ == "__main__":
    unittest.main()
