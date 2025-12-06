def calculate_average(students):
    result = {}

    for record in students:  # go through each student
        name = record['name']  # student name
        marks = record['marks']  # student marks list

        average = sum(marks) / len(marks)  # use sum() for total
        result[name] = average  # save in result

    return result


# Example
students = [
    {'name': 'Alice', 'marks': [78, 85, 62, 91]},
    {'name': 'Bob', 'marks': [55, 70, 58, 81]},
    {'name': 'Charlie', 'marks': [90, 92, 88, 95]},
    {'name': 'David', 'marks': [60, 65, 68, 71]},
    {'name': 'Eva', 'marks': [99, 94, 96, 100]}
]

print(calculate_average(students))