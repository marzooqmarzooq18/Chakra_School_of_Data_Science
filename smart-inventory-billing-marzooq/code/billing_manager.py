# billing_manager.py
import csv, os
from datetime import datetime
from code.context_manager import SafeFile
from code.utils import generate_bill_no, apply_discount_and_tax
from code.logger import log_info, log_error


BILLS_DIR = "data/bills"

# Ensure necessary directories exist
os.makedirs(os.path.dirname(BILLS_DIR), exist_ok=True)
os.makedirs(BILLS_DIR, exist_ok=True)

class BillingManager:
    """Manages billing operations."""

    def __init__(self):
        pass

    @apply_discount_and_tax(discount_rate=0.05, tax_rate=0.10)
    def calculate_total(self, items):
        """Calculate total amount for items before discount and tax."""
        return sum(float(item['price']) * int(item['quantity']) for item in items)

    def create_bill(self, items):
        """Generate a CSV bill file with all purchased items."""
        bill_no = generate_bill_no()
        total = self.calculate_total(items)
        bill_file = os.path.join(BILLS_DIR, f"{bill_no}.csv")

        try:
            with SafeFile(bill_file, "w") as f:
                writer = csv.writer(f)
                writer.writerow(["Product Name", "Price", "Quantity"])
                for item in items:
                    writer.writerow([item['name'], item['price'], item['quantity']])
                writer.writerow([])
                writer.writerow(["", "Total", total])
            log_info(f"Bill {bill_no} created successfully with total: {total}")
        except Exception as e:
            log_error(f"Failed to create bill: {e}")
        return bill_no, total


# --- Direct test run (optional) ---
if __name__ == "__main__":
    bm = BillingManager()
    sample_items = [
        {"name": "Pen", "price": "10", "quantity": "2"},
        {"name": "Notebook", "price": "50", "quantity": "1"},
    ]
    bill_no, total = bm.create_bill(sample_items)
    print(f"Bill {bill_no} created. Total = {total}")
