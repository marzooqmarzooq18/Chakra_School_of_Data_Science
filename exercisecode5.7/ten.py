# -------------------- Class: Student --------------------
class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.__fee_paid = 0

        # Assign total fee based on grade
        if grade == 10:
            self.__total_fee = 30000
        elif grade == 11:
            self.__total_fee = 35000
        else:
            self.__total_fee = 25000  # default for other grades

    def make_payment(self, amount):
        """Process student payment and handle overpayment."""
        remaining = self.get_balance()

        if amount <= 0:
            print(f"{self.name} → Invalid payment amount.")
            return 0

        if amount > remaining:
            print(f"{self.name} paid ₹{amount} (Extra amount detected! Refund initiated.)")
            self.__fee_paid = self.__total_fee  # Cap at total fee
            valid_payment = remaining  # Only add valid portion
        else:
            self.__fee_paid += amount
            print(f"{self.name} paid ₹{amount}")
            valid_payment = amount

        return valid_payment

    def get_balance(self):
        """Return remaining balance."""
        return self.__total_fee - self.__fee_paid

    def show_status(self):
        """Display student's payment summary."""
        balance = self.get_balance()
        print(f"Name: {self.name} | Grade: {self.grade} | Paid: ₹{self.__fee_paid} | Balance: ₹{balance}")


# -------------------- Class: FeeDepartment --------------------
class FeeDepartment:
    def __init__(self, department_name):
        self.department_name = department_name
        self.students = []
        self.__total_collection = 0

    def add_student(self, student):
        """Add student object to department."""
        self.students.append(student)

    def receive_fee(self, student, amount):
        """Accept payment from a student."""
        valid_amount = student.make_payment(amount)
        self.__total_collection += valid_amount

    def show_all_students(self):
        """Display all students' fee status."""
        print("\n--- Student Fee Status ---")
        for s in self.students:
            s.show_status()

    def get_total_collection(self):
        """Return total collected amount."""
        return self.__total_collection


# -------------------- Class: School --------------------
class School:
    def __init__(self, school_name, fee_department):
        self.school_name = school_name
        self.fee_department = fee_department

    def show_summary(self):
        """Display total students and total fee collection."""
        print("\n--- Department Summary ---")
        print(f"Total Fee Collection: ₹{self.fee_department.get_total_collection()}")


# -------------------- Demonstration --------------------
if __name__ == "__main__":
    # Create Fee Department
    accounts = FeeDepartment("Accounts Section")

    # Create Students
    s1 = Student(101, "Meena", 10)
    s2 = Student(102, "Raj", 11)
    s3 = Student(103, "Arjun", 10)

    # Add to Department
    accounts.add_student(s1)
    accounts.add_student(s2)
    accounts.add_student(s3)

    # --- Fee Payments ---
    print("--- Fee Payments ---")
    accounts.receive_fee(s1, 10000)
    accounts.receive_fee(s2, 20000)
    accounts.receive_fee(s3, 32000)

    # --- Show All Student Status ---
    accounts.show_all_students()

    # --- School Summary ---
    chakra_school = School("Chakra School", accounts)
    chakra_school.show_summary()