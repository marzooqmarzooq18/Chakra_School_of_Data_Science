items = [1, 2, 3, 4, 4, 5, 1]

unique_items = []

for item in items:
    if item not in unique_items:
        unique_items.append(item)

print(unique_items)

num = [1, 2, 3, 4, 5]
k = 2 # number of positions to rotate

for _ in range(k):
    last = num.pop() # Remove the last item
    num.insert(0, last) # Add it to the beginning

print(num)