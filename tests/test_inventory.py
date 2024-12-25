# test_inventory.py
import unittest

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from inventory import Inventory
from product import Product

class TestInventory(unittest.TestCase):

    def setUp(self):
        """Initialise l'inventaire et les produits pour chaque test."""
        self.inventory = Inventory()
        self.product1 = Product(name="Laptop", price=1200.0, stock=10)
        self.product2 = Product(name="Phone", price=500.0, stock=0)
        self.product3 = Product(name="Headphones", price=100.0, stock=3)

        # Ajouter les produits à l'inventaire
        self.inventory.add_product(self.product1)
        self.inventory.add_product(self.product2)
        self.inventory.add_product(self.product3)

    def test_display_available_products(self):
        """Teste l'affichage des produits disponibles en stock."""
        expected_output = (
            "Laptop - 10 in stock\n"
            "Phone - Out of stock\n"
            "Headphones - 3 in stock"
        )
        self.assertEqual(self.inventory.display_available_products(), expected_output)

    def test_product_added_to_inventory(self):
        """Vérifie que les produits sont ajoutés correctement à l'inventaire."""
        self.assertIn(self.product1, self.inventory.products)
        self.assertIn(self.product2, self.inventory.products)
        self.assertIn(self.product3, self.inventory.products)

    def test_no_products_in_inventory(self):
        """Vérifie le comportement lorsque l'inventaire est vide."""
        empty_inventory = Inventory()
        self.assertEqual(empty_inventory.display_available_products(), "")

if __name__ == "__main__":
    unittest.main()
