# Function to group employees by department
def group_by_department(employees):
    result = {}  # empty dictionary

    for emp, dept in employees:  # go through each (employee, department)
        if dept not in result:  # if department not yet in dictionary
            result[dept] = []  # make empty list
        result[dept].append(emp)  # add employee to department

    return result


# Example
employees = [
    ('Alice', 'HR'),
    ('Bob', 'IT'),
    ('Charlie', 'HR'),
    ('David', 'Finance'),
    ('Eve', 'Finance'),
    ('Frank', 'IT'),
    ('Grace', 'HR')
]

print(group_by_department(employees))