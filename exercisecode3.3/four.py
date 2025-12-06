customers = [
    {'name': 'Ajay', 'purchases': 4, 'amount': 72000},
    {'name': 'Priya', 'purchases': 8, 'amount': 51000},
    {'name': 'Vineet', 'purchases': 9, 'amount': 49999},
    {'name': 'Rahul', 'purchases': 15, 'amount': 150000},
    {'name': 'Asha', 'purchases': 6, 'amount': 65000},
    {'name': 'Leela', 'purchases': 3, 'amount': 35000},
    {'name': 'Kiran', 'purchases': 10, 'amount': 57000},
    {'name': 'Sanju', 'purchases': 11, 'amount': 52000},
    {'name': 'Mary', 'purchases': 5, 'amount': 70000},
    {'name': 'Ramesh', 'purchases': 12, 'amount': 45000},
    {'name': 'Fatima', 'purchases': 7, 'amount': 90000},
    {'name': 'Saurabh', 'purchases': 4, 'amount': 50000},
    {'name': 'Riya', 'purchases': 6, 'amount': 35000},
    {'name': 'Sunil', 'purchases': 11, 'amount': 51000},
    {'name': 'Nisha', 'purchases': 9, 'amount': 63000},
]

# Filter high-value customers
# Criteria: 'purchases' > 5 AND 'amount' > 50000
high_value_customers = [
    c for c in customers
    if c['purchases'] > 5 and c['amount'] > 50000
]

print(high_value_customers)