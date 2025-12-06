def custom_map(func, *iterables) -> list:
    """
    Applies 'func' to the elements of one or more iterables.
    Stops when the shortest iterable ends.
    Returns a list of results.
    """

    # Step 1: Check if func is callable
    if not callable(func):
        raise TypeError("The first argument must be a callable function.")

    # Step 2: Use zip() to combine elements from all iterables
    # zip() automatically stops at the shortest iterable
    result = []

    for items in zip(*iterables):
        # Step 3: Apply the function to the current set of elements
        value = func(*items)
        result.append(value)

    # Step 4: Return a new list of transformed values
    return result


# -------------------- Test Cases --------------------

# Example 1 - Single iterable
def square(x):
    return x * x

print(custom_map(square, [1, 2, 3, 4]))  # Expected Output: [1, 4, 9, 16]


# Example 2 - Multiple iterables
def add(a, b):
    return a + b

print(custom_map(add, [1, 2, 3], [10, 20, 30, 40]))  # Expected Output: [11, 22, 33]


# Example 3 - Empty iterable
def identity(x):
    return x

print(custom_map(identity, []))  # Expected Output: []


# -------------------- Reflection --------------------
print("What I learned about iterables and callables:")
print("I learned that iterables can be looped together using zip(), which stops at the shortest one.")
print("A callable is any object that can be called like a function, so it must be checked before use.")
print("By manually applying func to elements, I recreated map() in a simple and efficient way.")
