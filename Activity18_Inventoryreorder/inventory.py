class Product:
    def __init__(self, name, stock, min_stock):
        self.name = name
        self.stock = stock
        self.min_stock = min_stock

    def needs_reorder(self):
        """Return True if product stock is below the minimum threshold."""
        return self.stock < self.min_stock
