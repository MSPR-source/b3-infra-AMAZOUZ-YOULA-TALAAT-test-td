# Test : Affiche les produits disponibles en stock.
import unittest
import product
import inventory


class Inventory:
    def __init__(self):
        self.products = []  # Liste des produits

    def add_product(self, product):
        self.products.append(product)  # Ajouter un produit à l'inventaire

    def display_available_products(self):
        available_products = []
        for product in self.products:
            if product.stock > 0:
                available_products.append(f"{product.name} - {product.stock} in stock")
            else:
                available_products.append(f"{product.name} - Out of stock")
        return "\n".join(available_products)

if __name__ == "__main__":
    unittest.main(buffer=False)  # Disable buffering to display prints
