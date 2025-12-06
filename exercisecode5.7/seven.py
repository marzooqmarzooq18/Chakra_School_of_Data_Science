# -------------------- Class: Product --------------------
class Product:
    def __init__(self, name, price, quantity_available):
        self.name = name
        self.price = price
        self.quantity_available = quantity_available

    def show_product(self):
        """Display product details."""
        print(f"Product: {self.name} | Price: ₹{self.price} | Available: {self.quantity_available}")


# -------------------- Class: CartItem --------------------
class CartItem:
    def __init__(self, product, quantity):
        self.product = product      # Composition (Product object inside CartItem)
        self.quantity = quantity

    def get_total(self):
        """Return total cost for this item."""
        return self.product.price * self.quantity


# -------------------- Class: ShoppingCart --------------------
class ShoppingCart:
    def __init__(self):
        self.items = []   # list of CartItem objects

    def add_item(self, product, qty):
        """Add item to the cart if available."""
        if qty <= 0:
            print("Invalid quantity!")
            return
        if qty > product.quantity_available:
            print(f"Not enough stock for {product.name}! Only {product.quantity_available} left.")
            return

        # Create a CartItem and add it to the list
        item = CartItem(product, qty)
        self.items.append(item)
        print(f"Added {qty} x {product.name} @ ₹{product.price}")

    def calculate_total(self):
        """Compute total bill for all cart items."""
        total = sum(item.get_total() for item in self.items)
        return total

    def show_cart(self):
        """Display all cart items and total."""
        print("\nCart Summary:")
        for item in self.items:
            print(f"{item.product.name} - ₹{item.get_total()}")
        print(f"Total Bill: ₹{self.calculate_total()}")


# -------------------- Demonstration --------------------
if __name__ == "__main__":
    # Create some products
    p1 = Product("Laptop", 60000, 5)
    p2 = Product("Headphones", 3000, 10)
    p3 = Product("Smartwatch", 7000, 4)

    # Create a shopping cart
    cart = ShoppingCart()

    # Add products to the cart
    cart.add_item(p1, 2)  # 2 Laptops
    cart.add_item(p2, 1)  # 1 Headphone

    # Display cart summary
    cart.show_cart()