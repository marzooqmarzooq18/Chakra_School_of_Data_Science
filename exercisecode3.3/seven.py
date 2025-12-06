# Create a new dictionary of employees with salary > 50,000 across all departments.
departments = {
    'HR': {'John': 48000, 'Jane': 52000, 'Doe': 47000},
    'Engineering': {'Alice': 90000, 'Bob': 78000, 'Eve': 55000},
    'Sales': {'Mallory': 49000, 'Peggy': 60000, 'Trent': 58000}
}

high_salary = {
    name: salary  # name: salary is the key-value pair for the new dictionary
    for dept in departments.values()  # 1. Iterate over the department dictionaries (e.g., {'Jane': 52000, ...})
    for name, salary in dept.items()  # 2. Iterate over the (name, salary) pairs in the current department
    if salary > 50000  # 3. Apply the filter condition
}

print(high_salary)