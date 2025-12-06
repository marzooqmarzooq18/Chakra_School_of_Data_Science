def fibonacci_gen(limit: int):
    """
    Yields the first 'limit' Fibonacci numbers lazily (one at a time).
    Uses O(1) memory and avoids storing the entire sequence.
    """

    # Step 1: Handle invalid limits
    if limit <= 0:
        raise ValueError("limit must be a positive integer")

    # Step 2: Initialize first two Fibonacci numbers
    a, b = 0, 1

    # Step 3: Generate Fibonacci numbers one by one
    for _ in range(limit):
        yield a           # Return current Fibonacci number
        a, b = b, a + b   # Update values for next iteration


# -------------------- Test Cases --------------------

# Example 1 - Basic usage with for loop
print("Fibonacci sequence (7 numbers):")
for num in fibonacci_gen(7):
    print(num, end=" ")
print()  # Expected Output: 0 1 1 2 3 5 8


# Example 2 - Manual iteration using next()
print("\nManual iteration:")
gen = fibonacci_gen(5)
print(next(gen))   # Expected 0
print(next(gen))   # Expected 1
print(list(gen))   # Expected [1, 2, 3]


# Example 3 - Invalid limit
try:
    list(fibonacci_gen(0))
except ValueError as e:
    print("\nError:", e)  # Expected Output: ValueError: limit must be a positive integer


# -------------------- Reflection --------------------
print("\nHow generators optimize memory compared to lists:")
print("A generator produces one value at a time instead of storing all results in memory.")
print("This means fibonacci_gen(1000000) can run efficiently, since it only keeps two numbers (a and b) at any moment.")
print("In contrast, a list-based version would store all one million numbers, using much more memory.")
