# -------------------- Class: Course --------------------
class Course:
    def __init__(self, course_id, title, price):
        self.course_id = course_id
        self.title = title
        self.price = price

    def show_info(self):
        """Display course details."""
        print(f"Course ID: {self.course_id} | Title: {self.title} | Price: ₹{self.price}")


# -------------------- Class: Student --------------------
class Student:
    total_enrollments = 0  # Class variable shared across all students

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = []  # composition: holds Course objects

    def enroll(self, course):
        """Add a course to the student's enrolled list."""
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            Student.total_enrollments += 1
            print(f"{self.name} enrolled in {course.title}")
        else:
            print(f"{self.name} is already enrolled in {course.title}")

    def view_enrollments(self):
        """Show all enrolled course titles."""
        if not self.enrolled_courses:
            print(f"{self.name} has not enrolled in any courses yet.")
        else:
            print(f"\nCourses enrolled by {self.name}:")
            for course in self.enrolled_courses:
                print(f" - {course.title}")


# -------------------- Demonstration --------------------
if __name__ == "__main__":
    # Create course objects
    c1 = Course("C101", "Python Basics", 2500)
    c2 = Course("C102", "Data Analysis", 3000)
    c3 = Course("C103", "AWS Cloud Fundamentals", 3500)

    # Create student objects
    s1 = Student("S001", "Meena")
    s2 = Student("S002", "Raj")

    # Enroll students in courses
    s1.enroll(c1)
    s1.enroll(c2)
    s2.enroll(c3)

    # View each student's enrollments
    s1.view_enrollments()
    s2.view_enrollments()

    # Display total enrollments across all students
    print(f"\nTotal Enrollments: {Student.total_enrollments}")