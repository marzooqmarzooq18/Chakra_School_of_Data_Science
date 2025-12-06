class Employee:
    def __init__(self, emp_id, name, monthly_scores):
        self.emp_id = emp_id
        self.name = name
        self.monthly_scores = monthly_scores

    def calculate_average(self):
        return sum(self.monthly_scores) / len(self.monthly_scores)

    def performance_band(self):
        avg = self.calculate_average()
        if avg >= 8:
            return "Outstanding"
        elif avg >= 5:
            return "Good"
        else:
            return "Needs Improvement"

    def display_info(self):
        avg = self.calculate_average()
        band = self.performance_band()
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Average Score: {avg:.2f}")
        print(f"Performance: {band}")
        print("-" * 40)
