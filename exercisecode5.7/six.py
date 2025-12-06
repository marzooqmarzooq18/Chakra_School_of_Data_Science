# -------------------- Class Definition --------------------
class Student:
    def __init__(self, name, roll_no, total_classes):
        self.name = name
        self.roll_no = roll_no
        self.total_classes = total_classes
        self.attended_classes = 0
        self.__attendance_percent = 0.0   # private variable

    # -------------------- Core Methods --------------------
    def mark_attendance(self):
        """Mark student present for a class."""
        if self.attended_classes < self.total_classes:
            self.attended_classes += 1
        else:
            print(f"{self.name} has already attended all classes.")

    def calculate_percentage(self):
        """Compute and update attendance percentage."""
        if self.total_classes > 0:
            self.__attendance_percent = (self.attended_classes / self.total_classes) * 100
        else:
            self.__attendance_percent = 0.0
        return self.__attendance_percent

    def is_eligible(self):
        """Check if student can sit for exam (attendance ≥ 75%)."""
        return self.__attendance_percent >= 75

    def show_report(self):
        """Display the attendance report."""
        self.calculate_percentage()  # update before showing
        status = "Yes" if self.is_eligible() else "No"
        print(f"Name: {self.name} | Attendance: {self.__attendance_percent:.1f}% | Eligible: {status}")


# -------------------- Demonstration --------------------
if __name__ == "__main__":
    # Create student objects
    s1 = Student("Arjun", 101, total_classes=10)
    s2 = Student("Priya", 102, total_classes=10)
    s3 = Student("Karan", 103, total_classes=10)

    # Randomly mark attendance
    for _ in range(8):  # Arjun attended 8/10 classes → 80%
        s1.mark_attendance()

    for _ in range(7):  # Priya attended 7/10 classes → 70%
        s2.mark_attendance()

    for _ in range(9):  # simulate 9/10 classes → 90% (round down)
        s3.mark_attendance()

    # Display reports
    print()
    s1.show_report()
    s2.show_report()
    s3.show_report()