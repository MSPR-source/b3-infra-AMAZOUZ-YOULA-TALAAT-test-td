import unittest
import sys
import os

# Ajout du chemin du répertoire parent pour trouver `usercommand.py`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from usercommand import UserCommand  # Importation de la classe

class TestUserCommand(unittest.TestCase):
    def setUp(self):
        """Prépare un utilisateur et une commande pour les tests."""
        print("\n[SETUP] Initialisation d'un utilisateur et d'une commande pour les tests.")
        self.user_command = UserCommand("Alice", 100.0)  # On crée un utilisateur avec une commande de 100€

    def test_user_creation(self):
        """Teste la création d'un utilisateur et la vérification de son niveau initial."""
        print("[TEST] Vérification de la création d'un utilisateur.")
        self.assertEqual(self.user_command.name, "Alice")  # Vérifie le nom de l'utilisateur
        self.assertEqual(self.user_command.level, "Bronze")  # Vérifie le niveau initial

    def test_apply_discount(self):
        """Teste l'application d'une remise à la commande."""
        print("[TEST] Vérification de l'application d'une remise de 10%.")
        self.user_command.apply_discount(10)  # Applique une remise de 10%
        self.assertEqual(self.user_command.final_total, 90.0)  # Le total final devrait être 90 après remise

    def test_spend_points(self):
        """Teste l'utilisation des points pour une réduction."""
        print("[TEST] Vérification de l'utilisation des points.")
        self.user_command.add_points(50)  # Ajoute 50 points à l'utilisateur
        self.user_command.apply_discount(10)  # Applique une remise de 10% (100 - 10 = 90)
        self.user_command.spend_points(20)  # L'utilisateur utilise 20 points (soit 2€ de réduction)
        self.assertEqual(self.user_command.final_total, 88.0)  # 90 - 2 = 88

    def test_finalize_order(self):
        """Teste la finalisation de la commande."""
        print("[TEST] Finalisation de la commande.")
        self.user_command.apply_discount(10)  # Applique une remise de 10% (100 - 10 = 90)
        self.user_command.spend_points(20)  # Utilisation de points pour réduction
        self.user_command.finalize_order()  # Finalise la commande
        self.assertEqual(self.user_command.total_spent, 88.0)  # Vérifie que le total dépensé est mis à jour
        self.assertEqual(self.user_command.level, "Bronze")  # Le niveau reste "Bronze" car total_spent < 500

    def test_view_order_history(self):
        """Teste l'affichage de l'historique des commandes."""
        print("[TEST] Vérification de l'historique des commandes.")
        self.user_command.finalize_order()  # Finalise la commande
        self.user_command.view_order_history()  # Affiche l'historique des commandes
        # Ici, on devrait voir l'historique de commandes avec le total payé et les points gagnés

if __name__ == "__main__":
    print("[INFO] Lancement des tests unitaires pour UserCommand.")
    unittest.main()
