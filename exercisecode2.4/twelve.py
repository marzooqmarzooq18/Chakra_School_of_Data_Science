# Function to find the most frequent product
def most_frequent_product(purchases):
    counts = {}  # dictionary to count products

    # Count how many times each product appears
    for _, product in purchases:
        counts[product] = counts.get(product, 0) + 1

    # Find product with maximum count
    most_frequent = max(counts, key=counts.get)

    return most_frequent


# Example
purchases = [
    (1, 'Book'), (2, 'Pen'), (3, 'Book'), (4, 'Pencil'),
    (2, 'Pen'), (3, 'Book'), (5, 'Box'), (6, 'Pen'), (7, 'Book'),
    (8, 'Book'), (9, 'Pen'), (1, 'Pen'), (2, 'Pencil'), (3, 'Book'),
    (4, 'Book'), (5, 'Pen'), (6, 'Book'), (7, 'Notebook'), (1, 'Book'),
    (2, 'Box'), (3, 'Pen'), (4, 'Book'), (5, 'Pen'), (6, 'Pencil'),
    (7, 'Book'), (8, 'Notebook'), (9, 'Book'), (1, 'Book'), (2, 'Box')
]

print(most_frequent_product(purchases))