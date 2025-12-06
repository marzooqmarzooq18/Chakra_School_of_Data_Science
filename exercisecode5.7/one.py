from datetime import datetime

class DigitalWallet:
    # Class variable for tracking total transactions
    transaction_count = 0

    def __init__(self, wallet_id, owner_name):
        self.wallet_id = wallet_id
        self.owner_name = owner_name
        self.__balance = 0          # private attribute (encapsulation)
        self.transactions = []      # list to store all transaction logs
        print(f"Wallet created for: {self.owner_name}")

    # ---------------- Encapsulation Methods ----------------
    def get_balance(self):
        """Return the current wallet balance."""
        return self.__balance

    # ---------------- Static Validation Method ----------------
    @staticmethod
    def validate_transaction(amount):
        """Return True if amount is valid (greater than 0)."""
        return amount > 0

    # ---------------- Core Operations ----------------
    def add_money(self, amount):
        """Add money to the wallet after validating."""
        if not self.validate_transaction(amount):
            print("Invalid amount! Please enter a positive value.")
            return

        self.__balance += amount
        DigitalWallet.transaction_count += 1
        self.transactions.append(("ADD_MONEY", amount, "Self", datetime.now()))
        print(f"Deposited ₹{amount}")

        # Check for cashback
        self.__apply_cashback_if_needed()

    def pay(self, receiver, amount):
        """Send money to another person if balance is sufficient."""
        if not self.validate_transaction(amount):
            print("Invalid amount! Please enter a positive value.")
            return

        if amount > self.__balance:
            print("Transaction failed! Insufficient balance.")
            return

        self.__balance -= amount
        DigitalWallet.transaction_count += 1
        self.transactions.append(("PAYMENT", amount, receiver, datetime.now()))
        print(f"Sent ₹{amount} to {receiver}")

        # Check for cashback
        self.__apply_cashback_if_needed()

    # ---------------- Cashback Logic ----------------
    def __apply_cashback_if_needed(self):
        """Apply 1% cashback after every 5th transaction."""
        if DigitalWallet.transaction_count % 5 == 0:
            cashback = self.__balance * 0.01  # 1% of current balance
            self.__balance += cashback
            self.transactions.append(("CASHBACK", round(cashback, 2), "System", datetime.now()))
            print(f"CASHBACK ₹{round(cashback, 2)} credited!")

    # ---------------- Statement Printing ----------------
    def get_statement(self, n=5):
        """Display the last N transactions."""
        print("\n--- Recent Transactions ---")
        recent = self.transactions[-n:]
        for i, (t_type, amount, party, time) in enumerate(recent, start=1):
            time_str = time.strftime("%Y-%m-%d %H:%M")
            if t_type == "ADD_MONEY":
                print(f"{i}. {t_type} ₹{amount} | {time_str}")
            elif t_type == "PAYMENT":
                print(f"{i}. {t_type} ₹{amount} | To: {party} | {time_str}")
            elif t_type == "CASHBACK":
                print(f"{i}. {t_type} ₹{amount} | From: {party}")
        print("---------------------------")


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    wallet = DigitalWallet("W123", "Arjun")

    wallet.add_money(2000)
    wallet.pay("Sneha", 500)
    wallet.add_money(1000)
    wallet.pay("Rahul", 300)
    wallet.pay("Neha", 200)   # This will trigger the 5th transaction cashback

    print(f"\nAvailable Balance: ₹{wallet.get_balance()}")
    wallet.get_statement()