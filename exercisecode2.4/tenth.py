# Function to check if a student passes
def is_passing(scores, pass_mark):
    for s in scores:
        if s < pass_mark:   # if any score is below pass mark
            return False
    return True             # all scores are above or equal to pass mark


# Function to get names of passing students
def get_passing_students(students, pass_mark):
    result = []
    for student in students:
        if is_passing(student['scores'], pass_mark):  # use helper function
            result.append(student['name'])
    return result


# Example
students = [
    {'name': 'John', 'scores': [80, 75, 90, 85]},
    {'name': 'Jane', 'scores': [50, 40, 60, 55]},
    {'name': 'Doe', 'scores': [55, 65, 70, 60]},
    {'name': 'Anna', 'scores': [45, 50, 48, 52]},
    {'name': 'Mark', 'scores': [90, 92, 88, 95]},
    {'name': 'Paul', 'scores': [30, 40, 20, 35]},
    {'name': 'Nina', 'scores': [65, 70, 60, 55]},
    {'name': 'Sam', 'scores': [55, 58, 54, 59]}
]

pass_mark = 50
print(get_passing_students(students, pass_mark))