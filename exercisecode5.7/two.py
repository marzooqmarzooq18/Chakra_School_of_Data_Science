import re


class Student:
    # Class variable to track total number of students
    student_count = 0

    def __init__(self, name, roll_no):
        # Validate name using static method
        if not Student.validate_name(name):
            raise ValueError("Invalid name! Only alphabets and spaces are allowed.")

        self.name = name
        self.roll_no = roll_no
        self.__marks = {}  # private dictionary for marks
        Student.student_count += 1

    # ---------------- Encapsulation Methods ----------------
    def add_mark(self, subject, score):
        """Add a subject mark if score is valid."""
        if 0 <= score <= 100:
            self.__marks[subject] = score
        else:
            print(f"Invalid score for {subject}! Enter between 0 and 100.")

    def get_average(self):
        """Return the average of all subject marks."""
        if len(self.__marks) == 0:
            return 0
        return sum(self.__marks.values()) / len(self.__marks)

    def get_grade(self):
        """Return grade based on average marks."""
        avg = self.get_average()
        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "Fail"

    def display_report(self):
        """Print formatted report card."""
        print(f"\nStudent: {self.name} | Roll: {self.roll_no}")
        print(f"Added Marks: {self.__marks}")
        avg = round(self.get_average(), 2)
        grade = self.get_grade()
        print(f"Average: {avg}")
        print(f"Grade: {grade}")

    # ---------------- Static & Class Methods ----------------
    @staticmethod
    def validate_name(name):
        """Return False if name has special characters or numbers."""
        pattern = r"^[A-Za-z ]+$"
        return re.match(pattern, name) is not None

    @classmethod
    def get_total_students(cls):
        """Return total number of students created."""
        return cls.student_count


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    # Create some students
    s1 = Student("Meena", 102)
    s1.add_mark("Math", 95)
    s1.add_mark("Science", 89)
    s1.add_mark("English", 92)
    s1.display_report()

    s2 = Student("Arjun", 103)
    s2.add_mark("Math", 78)
    s2.add_mark("Science", 85)
    s2.add_mark("English", 80)
    s2.display_report()

    s3 = Student("Divya", 104)
    s3.add_mark("Math", 55)
    s3.add_mark("Science", 68)
    s3.add_mark("English", 61)
    s3.display_report()

    print(f"\nTotal Students: {Student.get_total_students()}")