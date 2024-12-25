import unittest

class User:
    def __init__(self, name: str):
        self.name = name
        self.first_order10 = True

    def mark_first_order10_done(self):
        self.first_order10 = False


class order10:
    def __init__(self, user: User, total: float):
        self.user = user
        self.original_total = total
        self.discounted_total = self.apply_welcome_discount()

    def apply_welcome_discount(self):
        if self.user.first_order10:
            return round(self.original_total * 0.9, 2)
        return round(self.original_total, 2)

    def finalize_order10(self):
        if self.user.first_order10:
            self.user.mark_first_order10_done()


class Testorder10(unittest.TestCase):

    def setUp(self):
        """Crée un utilisateur et une commande pour les tests."""
        self.user = User("Alice")
        self.order10 = order10(self.user, 100.0)  # Commande de 100€ pour un nouvel utilisateur

    def test_first_order10_discount(self):
        """Teste que la réduction de 10% est appliquée pour la première commande."""
        self.assertEqual(self.order10.discounted_total, 90.0)  # 10% de réduction sur 100€

    def test_first_order10_status(self):
        """Vérifie que l'état de l'utilisateur est mis à jour après la première commande."""
        self.order10.finalize_order10()  # Après avoir finalisé la commande, l'utilisateur ne doit plus avoir de première commande
        self.assertFalse(self.user.first_order10)  # L'utilisateur ne doit plus avoir de première commande

    def test_no_discount_after_first_order10(self):
        """Teste qu'aucune réduction n'est appliquée après la première commande."""
        self.order10.finalize_order10()  # Finalise la commande pour marquer la première commande comme terminée
        new_order10 = order10(self.user, 100.0)  # Crée une nouvelle commande après la première
        self.assertEqual(new_order10.discounted_total, 100.0)  # Pas de réduction après la première commande


if __name__ == "__main__":
    unittest.main()
