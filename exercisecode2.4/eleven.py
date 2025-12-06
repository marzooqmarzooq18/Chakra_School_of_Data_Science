# Function to get products above threshold
def products_above(prices, threshold):
    # filter items where value > threshold
    result = filter(lambda item: item[1] > threshold, prices.items())

    # collect only product names
    return [item[0] for item in result]


# Example
prices = {
    'pen': 10, 'notebook': 50, 'bag': 100, 'bottle': 80,
    'box': 30, 'laptop': 40000, 'mouse': 1200, 'keyboard': 1500,
    'chair': 2250, 'lamp': 900, 'monitor': 9000, 'printer': 7000
}

threshold = 1000
print(products_above(prices, threshold))