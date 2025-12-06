# Function to find discontinued or out-of-stock products
def find_unavailable(inventory):
    result = []  # empty list to store product IDs

    for item in inventory:  # loop through each dictionary in the list
        if item['discontinued'] == True or item['stock'] == 0:
            result.append(item['id'])  # add the product id to result

    return result


# Example
inventory = [
    {'id': 101, 'stock': 20, 'discontinued': False},
    {'id': 102, 'stock': 0, 'discontinued': True},
    {'id': 103, 'stock': 15, 'discontinued': False},
    {'id': 104, 'stock': 0, 'discontinued': False},
    {'id': 105, 'stock': 5, 'discontinued': True},
    {'id': 106, 'stock': 8, 'discontinued': False},
    {'id': 107, 'stock': 0, 'discontinued': False},
    {'id': 108, 'stock': 10, 'discontinued': False},
    {'id': 109, 'stock': 0, 'discontinued': True},
    {'id': 110, 'stock': 12, 'discontinued': False},
]

print(find_unavailable(inventory))