# debug_collections.py
numbers = [2, 4, 6, 8, 10]
squares = {}

for n in numbers:
    squares[n] = n ** 2
    print(f"Processed: {n}")

print("Final Squares:", squares)