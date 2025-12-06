def top_earners(employees, department, N):
    # Step 1: collect only employees in the given department
    dept_employees = []
    for emp in employees:
        if emp[1] == department:
            dept_employees.append(emp)

    result = []
    # Step 2: repeat N times to find the top earners
    for i in range(N):
        # find the employee with the highest salary
        highest = dept_employees[0]
        for emp in dept_employees:
            if emp[2] > highest[2]:
                highest = emp

        result.append(highest[0])  # add name to result
        dept_employees.remove(highest)  # remove so next highest can be found

    return result


# Example
employees = [
    ('Alice', 'HR', 50000), ('Bob', 'IT', 70000), ('Charlie', 'HR', 55000),
    ('David', 'IT', 60000), ('Eve', 'HR', 65000), ('Frank', 'Finance', 72000),
    ('Grace', 'IT', 75000), ('Heidi', 'HR', 48000), ('Ivan', 'Finance', 69000),
    ('Judy', 'HR', 53000), ('Karl', 'IT', 71000), ('Leo', 'HR', 51000)
]

department = 'HR'
N = 3

print(top_earners(employees, department, N))