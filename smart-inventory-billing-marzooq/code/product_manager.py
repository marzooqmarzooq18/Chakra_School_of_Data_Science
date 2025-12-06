# product_manager.py
import csv, os
from code.context_manager import SafeFile
from code.logger import log_info, log_error


DATA_FILE = "data/products.csv"

# Ensure data directory exists
os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

class ProductManager:
    """Handles product operations like add, update, delete, and view."""

    def __init__(self):
        if not os.path.exists(DATA_FILE):
            with SafeFile(DATA_FILE, "w") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "name", "price", "quantity"])

    def add_product(self, pid, name, price, quantity):
        try:
            with SafeFile(DATA_FILE, "a") as f:
                writer = csv.writer(f)
                writer.writerow([pid, name, price, quantity])
            log_info(f"Added product: {name}")
        except Exception as e:
            log_error(f"Failed to add product: {e}")

    def view_products(self):
        try:
            with SafeFile(DATA_FILE, "r") as f:
                reader = csv.DictReader(f)
                return list(reader)
        except Exception as e:
            log_error(f"Failed to view products: {e}")
            return []

    def update_product(self, pid, new_price=None, new_quantity=None):
        try:
            rows = []
            with SafeFile(DATA_FILE, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row["id"] == pid:
                        if new_price: row["price"] = str(new_price)
                        if new_quantity: row["quantity"] = str(new_quantity)
                    rows.append(row)
            with SafeFile(DATA_FILE, "w") as f:
                writer = csv.DictWriter(f, fieldnames=["id", "name", "price", "quantity"])
                writer.writeheader()
                writer.writerows(rows)
            log_info(f"Updated product {pid}")
        except Exception as e:
            log_error(f"Failed to update product: {e}")

    def delete_product(self, pid):
        try:
            rows = []
            with SafeFile(DATA_FILE, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row["id"] != pid:
                        rows.append(row)
            with SafeFile(DATA_FILE, "w") as f:
                writer = csv.DictWriter(f, fieldnames=["id", "name", "price", "quantity"])
                writer.writeheader()
                writer.writerows(rows)
            log_info(f"Deleted product {pid}")
        except Exception as e:
            log_error(f"Failed to delete product: {e}")

# --- Helper wrapper for test integration ---
def add_product(pid, name, price, quantity):
    pm = ProductManager()
    pm.add_product(pid, name, price, quantity)

# --- Direct test run (optional) ---
if __name__ == "__main__":
    pm = ProductManager()
    pm.add_product("101", "TestPen", 10, 100)
    print(pm.view_products())
