class DeliveryCalculator:
    # Initialisation de la classe avec les paramètres de calcul
    def __init__(self, free_shipping_threshold=100.0, weight_rate=2.0, base_rate=5.0):
        self.free_shipping_threshold = free_shipping_threshold
        self.weight_rate = weight_rate
        self.base_rate = base_rate

    # Représentation en chaîne de caractères pour faciliter le débogage
    def __str__(self):
        return f"Free Shipping Threshold: {self.free_shipping_threshold}€, Weight Rate: {self.weight_rate}€/kg, Base Rate: {self.base_rate}€"

    # Méthode pour calculer les frais de livraison
    def calculate_shipping_cost(self, total_price, total_weight):
        if total_price >= self.free_shipping_threshold:
            return 0.0  # Livraison gratuite
        return self.base_rate + (self.weight_rate * total_weight)  # Tarif de base + tarif par kilogramme

