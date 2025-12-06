# main.py
from atm import login, deposit, withdraw, check_balance

def main():
    acc = login()
    if not acc:
        return

    while True:
        print("\n===== ATM Menu =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            deposit(acc)
        elif choice == "2":
            withdraw(acc)
        elif choice == "3":
            check_balance(acc)
        elif choice == "4":
            print("👋 Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
