# test_inventory.py
import unittest

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from inventory import Inventory
from product import Product

class TestInventory(unittest.TestCase):

    def setUp(self):
        "Initialise l'inventaire et les produits pour chaque test."
        print("[Setup] Created Inventory and Product instances for testing.")

        self.inventory = Inventory()
        self.product1 = Product(name="Laptop", price=1200.0, stock=10)
        self.product2 = Product(name="Phone", price=500.0, stock=0)
        self.product3 = Product(name="Headphones", price=100.0, stock=3)

        # Ajouter les produits à l'inventaire
        self.inventory.add_product(self.product1)
        self.inventory.add_product(self.product2)
        self.inventory.add_product(self.product3)

    def test_display_available_products(self):
        "Teste l'affichage des produits disponibles en stock."
        print("[Test] Testing display of available products...")
        expected_output = (
            "Laptop - 10 in stock\n"
            "Phone - Out of stock\n"
            "Headphones - 3 in stock"
        )
        result = self.inventory.display_available_products()
        print(f"[Test] Expected output:\n{expected_output}")
        print(f"[Test] Actual output:\n{result}")
        self.assertEqual(result, expected_output)
        print("[Test] Display available products passed.")


    def test_product_added_to_inventory(self):
        "Vérifie que les produits sont ajoutés correctement à l'inventaire."
        print("[Test] Testing product addition to inventory...")
        self.assertIn(self.product1, self.inventory.products)
        self.assertIn(self.product2, self.inventory.products)
        self.assertIn(self.product3, self.inventory.products)
        print("[Test] Product addition to inventory passed.")


    def test_no_products_in_inventory(self):
        print("[Setup] Created an empty Inventory instance for testing.")
        empty_inventory = Inventory()
        print("[Test] Testing behavior with no products in inventory...")
        result = empty_inventory.display_available_products()
        print(f"[Test] Expected output: '' (empty string)")
        print(f"[Test] Actual output: '{result}'")
        self.assertEqual(result, "")
        print("[Test] No products in inventory test passed.")

if __name__ == "__main__":
    unittest.main(buffer=False)
