# order10.py

from cart import Cart

class order10:
    def __init__(self, cart: Cart):
        if not cart.items:
            raise ValueError("Cart is empty. Cannot place an order10.")
        self.items = cart.items
        self.total = cart.calculate_total()

    def place_order10(self):
        for product, quantity in self.items.items():
            product.reduce_stock(quantity)
        return f"order10 placed successfully! Total: {self.total:.2f}€"

    def view_order10(self):
        return "\n".join([f"{product.name} x {quantity}" for product, quantity in self.items.items()]) + \
               f"\nTotal: {self.total:.2f}€"
