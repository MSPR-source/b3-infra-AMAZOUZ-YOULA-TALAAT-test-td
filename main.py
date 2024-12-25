# main.py

from product import Product
from cart import Cart
from order10 import order10

def main():
    # Create products
    p1 = Product("Laptop", 1200.0, 5)
    p2 = Product("Headphones", 150.0, 20)
    p3 = Product("Mouse", 25.0, 50)

    # Initialize a cart
    cart = Cart()

    # Add products to the cart
    try:
        cart.add_product(p1, 1)
        cart.add_product(p2, 2)
    except ValueError as e:
        print(f"Error: {e}")

    print("Cart:")
    print(cart.display_cart())

    # Place an order10
    try:
        order10 = order10(cart)
        print("\norder10:")
        print(order10.view_order10())
        print(order10.place_order10())
    except ValueError as e:
        print(f"Error: {e}")

    # Check remaining stock
    print("\nStock after order10:")
    print(p1)
    print(p2)
    print(p3)

if __name__ == "__main__":
    main()
