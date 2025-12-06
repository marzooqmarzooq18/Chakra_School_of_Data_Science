# encapsulation_demo.py
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner        # public
        self._balance = balance   # protected (naming convention)
        self.__pin = "1234"       # private (name-mangled)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def show_balance(self):
        print(f"Balance for {self.owner}: ₹{self._balance}")

def main():
    acc1 = BankAccount("Arun", 5000)
    acc1.show_balance()

    # Try direct access (not recommended)
    print(acc1._balance)      # allowed but discouraged
    print(acc1.__pin)         # should raise error

main()