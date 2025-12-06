# oop_structure_demo.py
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_detail(self):
        print(f"Employee: {self.name}, Salary: ₹{self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def show_detail(self):
        super().show_detail()
        print(f"Team Size: {self.team_size}")

def main():
    emp1 = Employee("Arun", 50000)
    # mgr1 = Manager("Meera", 65000, 5)

    emp1.show_detail()
    # mgr1.display_info()

main()