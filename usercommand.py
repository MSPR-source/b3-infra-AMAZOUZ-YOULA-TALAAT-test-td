class UserCommand:
    def __init__(self, name: str, total: float):
        self.name = name
        self.total_spent = 0
        self.points = 0
        self.level = "Bronze"  # Remplacement de 'tier' par 'level'
        self.orders = []
        self.original_total = total
        self.final_total = total
        print(f"[INFO] Utilisateur créé : {self.name}, Level initial : {self.level}")

    def add_points(self, points: int):
        self.points += points
        print(f"[INFO] {self.name} a gagné {points} points. Total de points : {self.points}")

    def upgrade_level(self):
        if self.total_spent > 1000:
            self.level = "Gold"
        elif self.total_spent > 500:
            self.level = "Silver"
        print(f"[INFO] Level actuel de {self.name} : {self.level}")

    def apply_discount(self, percentage: float):
        discount = self.original_total * (percentage / 100)
        self.final_total -= discount
        print(f"[PROMO] Une remise de {percentage}% a été appliquée. Nouveau total : {self.final_total}€")

    def spend_points(self, points: int):
        discount = points * 0.1  # 1 point = 0.10€
        if discount > self.final_total:
            print(f"[ERREUR] Impossible d'utiliser autant de points.")
        else:
            self.final_total -= discount
            self.points -= points
            print(f"[INFO] {points} points utilisés. Nouveau total : {self.final_total}€")

    def finalize_order(self):
        self.total_spent += self.final_total
        points_gained = int(self.final_total // 10)  # Gagner des points (1 point par 10€ dépensé)
        self.add_points(points_gained)  # Gagner des points
        self.upgrade_level() #ajoute les détails de la commande à l'historique
        # Ajouter la commande à l'historique des commandes
        self.orders.append({            
        "total": self.final_total,
        "points_gained": points_gained,
        "level_after_order": self.level,
        })
        print(f"[INFO] Commande finalisée pour {self.name}. Total payé : {self.final_total}€")

    
    def view_order_history(self):
        print(f"[INFO] Historique des commandes de {self.name}:")
        for order in self.orders:
            print(f"  - Total : {order['total']}€, Points gagnés : {order['points_gained']}, Niveau après commande : {order['level_after_order']}")

