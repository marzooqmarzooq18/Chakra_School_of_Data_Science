from performance import Employee

def main():
    employees = [
        Employee(101, "Aditi", [8, 9, 7, 10]),
        Employee(102, "Rahul", [6, 7, 5, 6]),
        Employee(103, "Meena", [4, 5, 3, 4]),
        Employee(104, "Zain", [9, 9, 8, 10])
    ]

    print("Employee Performance Evaluation Report\n")
    for emp in employees:
        emp.display_info()

if __name__ == "__main__":
    main()
