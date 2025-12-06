products = [
    {'id': 'P001', 'price': 1500, 'available': True},
    {'id': 'P002', 'price': 750, 'available': True},
    {'id': 'P003', 'price': 1200, 'available': False},
    {'id': 'P004', 'price': 1300, 'available': True},
    {'id': 'P005', 'price': 1040, 'available': True},
    {'id': 'P006', 'price': 950, 'available': False},
]

# Create a list of tuples (id, price with tax)
# The tax rate is 18%, calculated as price * 1.18
result = [
    (p['id'], p['price'] * 1.18)  # Expression: creates the tuple
    for p in products  # Loop: iterates through each product dictionary
    if p['price'] > 1000 and p['available']  # Filter: price > 1000 AND available is True
]

print(result)