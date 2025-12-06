class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calc_average(self):
        """Return the average percentage of the student."""
        return sum(self.marks) / len(self.marks)

    def grade(self):
        """Assign grade based on average percentage."""
        avg = self.calc_average()
        if avg >= 85:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "D"
