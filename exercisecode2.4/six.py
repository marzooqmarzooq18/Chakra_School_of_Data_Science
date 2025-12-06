def total_expenses(expenses):
    result = {}
    for category in expenses:               # go through each category
        result[category] = sum(expenses[category])  # directly sum the list
    return result


# Example
expenses = {
    'rent': [1200, 1200, 1200, 1200],
    'food': [300, 250, 400, 320, 280, 350],
    'transport': [100, 90, 110, 105],
    'utilities': [150, 160, 140, 130],
    'entertainment': [200, 180, 210, 220]
}

print(total_expenses(expenses))