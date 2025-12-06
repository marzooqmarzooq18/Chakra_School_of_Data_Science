# utils.py
import os
from datetime import datetime
from code.logger import log_info, log_error


def generate_bill_no():
    """
    Generate a unique bill number using the current date and a sequence counter.
    Example: B20251106_001
    """
    try:
        date_part = datetime.now().strftime("%Y%m%d")
        counter_file = "data/bill_counter.txt"
        os.makedirs("data", exist_ok=True)

        # Read the current counter
        if os.path.exists(counter_file):
            with open(counter_file, "r") as f:
                count = int(f.read().strip() or 0)
        else:
            count = 0

        # Increment and save the new counter
        count += 1
        with open(counter_file, "w") as f:
            f.write(str(count))

        bill_no = f"B{date_part}_{count:03d}"
        return bill_no

    except Exception as e:
        log_error(f"Error generating bill number: {e}")
        return "B00000000_000"


def apply_discount_and_tax(discount_rate=0.05, tax_rate=0.10):
    """
    Decorator to apply discount and tax on total amount.
    Discount applied first, then tax.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                subtotal = func(*args, **kwargs)
                discounted = subtotal * (1 - discount_rate)
                total = discounted * (1 + tax_rate)
                total_rounded = round(total, 2)
                log_info(
                    f"Subtotal: {subtotal}, Discount: {discount_rate*100}%, "
                    f"Tax: {tax_rate*100}%, Final Total: {total_rounded}"
                )
                return total_rounded
            except Exception as e:
                log_error(f"Error in discount/tax calculation: {e}")
                return 0.0
        return wrapper
    return decorator
