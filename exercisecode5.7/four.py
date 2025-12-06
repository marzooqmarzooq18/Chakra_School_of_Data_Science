# -------------------- Base Class --------------------
class Employee:
    def __init__(self, emp_id, name, base_salary=0):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        """Default method (to be overridden)."""
        return 0

    def show_info(self):
        """Display employee basic info."""
        print(f"Employee ID: {self.emp_id} | Name: {self.name}", end=" | ")


# -------------------- Subclass 1: Full-Time --------------------
class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, base_salary, bonus_percent):
        super().__init__(emp_id, name, base_salary)
        self.bonus_percent = bonus_percent

    def calculate_salary(self):
        """Full-time salary = base + bonus."""
        return self.base_salary + (self.base_salary * self.bonus_percent / 100)


# -------------------- Subclass 2: Part-Time --------------------
class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        """Part-time salary = hourly_rate × hours_worked."""
        return self.hourly_rate * self.hours_worked


# -------------------- Subclass 3: Intern --------------------
class Intern(Employee):
    def __init__(self, emp_id, name, stipend):
        super().__init__(emp_id, name)
        self.stipend = stipend

    def calculate_salary(self):
        """Intern salary = fixed stipend."""
        return self.stipend


# -------------------- Polymorphic Payroll Calculation --------------------
if __name__ == "__main__":
    # Create employee objects of different types
    emp1 = FullTimeEmployee(101, "Arjun", 50000, 4)
    emp2 = PartTimeEmployee(102, "Priya", 300, 60)
    emp3 = Intern(103, "Ravi", 8000)

    # Store in one list (polymorphism)
    employees = [emp1, emp2, emp3]

    # Loop through and call methods without checking type
    for emp in employees:
        emp.show_info()
        print(f"Salary: {int(emp.calculate_salary())}")