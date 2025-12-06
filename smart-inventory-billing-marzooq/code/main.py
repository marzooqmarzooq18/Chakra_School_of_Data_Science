from auth_manager import AuthManager
from product_manager import ProductManager
from billing_manager import BillingManager

def main():
    print("=== Smart Inventory & Billing System ===")

    # Step 1: User Authentication
    auth = AuthManager()
    print("\n1. Login\n2. Register")
    choice = input("Select option: ")

    if choice == "2":
        auth.register_user()
        return
    elif choice != "1":
        print("Invalid choice.")
        return

    if not auth.login_user():
        print("Access denied. Please try again.")
        return

    # Step 2: Initialize Managers
    pm = ProductManager()
    bm = BillingManager()

    # Step 3: Main Menu Loop
    while True:
        print("\n=== Main Menu ===")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Create Bill")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            pid = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = input("Enter price: ")
            qty = input("Enter quantity: ")
            pm.add_product(pid, name, price, qty)
            print(" Product added successfully.")

        elif choice == "2":
            products = pm.view_products()
            if not products:
                print("No products found.")
            else:
                print("\n--- Product List ---")
                for p in products:
                    print(p)

        elif choice == "3":
            pid = input("Enter product ID to update: ")
            price = input("Enter new price (blank to skip): ")
            qty = input("Enter new quantity (blank to skip): ")
            pm.update_product(pid, price if price else None, qty if qty else None)
            print(" Product updated.")

        elif choice == "4":
            pid = input("Enter product ID to delete: ")
            pm.delete_product(pid)
            print(" Product deleted.")

        elif choice == "5":
            print("\n--- Create Bill ---")
            print("Enter items for billing (type 'done' to finish):")
            items = []
            while True:
                name = input("Product name: ")
                if name.lower() == "done":
                    break
                price = input("Price: ")
                qty = input("Quantity: ")
                items.append({"name": name, "price": price, "quantity": qty})

            if not items:
                print("No items entered. Bill not created.")
            else:
                bill_no, total = bm.create_bill(items)
                print(f"\n Bill {bill_no} created successfully.")
                print(f" Total Amount: ₹{total}")

        elif choice == "6":
            print("Exiting system. Goodbye!")
            break

        else:
            print(" Invalid option. Try again.")


if __name__ == "__main__":
    main()
