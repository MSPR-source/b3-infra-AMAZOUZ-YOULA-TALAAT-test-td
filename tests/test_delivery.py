import unittest

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from delivery import DeliveryCalculator

class TestDeliveryCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = DeliveryCalculator(free_shipping_threshold=100.0, weight_rate=2.0, base_rate=5.0)
        print("\n[Setup] Created a product instance for testing.")

    def test_DeliveryCalculator_initialization(self):
        print("[Test] Testing DeliveryCalculator Initialization...")
        self.assertEqual(self.calculator.free_shipping_threshold, 100.0)
        self.assertEqual(self.calculator.weight_rate, 2.0)
        self.assertEqual(self.calculator.base_rate, 5.0)
        print("[Test] DeliveryCalculator Initialization passed.")

 # Test que la livraison est gratuite lorsque le seuil est atteint.

    def test_free_shipping(self):
        print("[test] testing free_shipping (success case)...")
        self.assertEqual(self.calculator.calculate_shipping_cost(120.0, 10.0), 0.0)
        print("[test] testing free_shipping (success case) passed.")

 # Test que les frais de livraison sont correctement calculés lorsque le seuil n'est pas atteint.

    def test_shipping_cost_calculation(self):
        print("[test] testing shipping_cost_calculation (success case)...")
        self.assertEqual(self.calculator.calculate_shipping_cost(50.0, 10.0), 25.0)  # 5.0 + (2.0 * 10.0)
        print("[test] testing shipping_cost_calculation (success case) passed.")
 
 #Test que le tarif de base est appliqué pour les poids faibles.

    def test_minimum_shipping_cost(self):
        print("[test] testing minimum_shipping_cost (success case) passed.")
        self.assertEqual(self.calculator.calculate_shipping_cost(30.0, 1.0), 7.0)  # 5.0 + (2.0 * 1.0)
        print("[test] testing minimum_shipping_cost (success case) passed.")

if __name__ == "__main__":
    unittest.main()