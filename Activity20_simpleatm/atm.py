# atm.py

users = {
    "1001": {"pin": "1234", "balance": 5000},
    "1002": {"pin": "4321", "balance": 8000}
}

def login():
    acc = input("Enter Account Number: ")
    pin = input("Enter PIN: ")
    if acc in users and users[acc]["pin"] == pin:
        print("✅ Login successful!")
        return acc
    else:
        print(" Invalid credentials.")
        return None

def deposit(acc):
    amt = float(input("Enter amount to deposit: "))
    users[acc]["balance"] += amt
    print(f" Deposited ₹{amt}. New Balance: ₹{users[acc]['balance']}")

def withdraw(acc):
    amt = float(input("Enter amount to withdraw: "))
    if amt <= users[acc]["balance"]:  # ← Set breakpoint here
        users[acc]["balance"] -= amt
        print(f"💸 Withdrawn ₹{amt}. Remaining Balance: ₹{users[acc]['balance']}")
    else:
        print(" Insufficient balance!")

def check_balance(acc):
    print(f"🏦 Current Balance: ₹{users[acc]['balance']}")
