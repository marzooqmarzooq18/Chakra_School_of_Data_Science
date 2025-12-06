from typing import Callable, Iterable, Any

def custom_reduce(func: Callable, iterable: Iterable, initializer: Any = None):
    """
    Applies 'func' cumulatively to items of 'iterable', optionally starting
    with an initial value. Mimics functools.reduce() in a simple way.

    Args:
        func (Callable): A binary function taking two arguments (accumulator, item).
        iterable (Iterable): An iterable of items to reduce.
        initializer (Any, optional): Starting value for the accumulator. If None,
                                     the first item of iterable is used.

    Returns:
        Any: The final reduced value.

    Raises:
        TypeError: If func is not callable.
        TypeError: If iterable is not iterable.
        TypeError: If iterable is empty and no initializer is provided.
    Note:
        For simplicity this implementation treats initializer=None the same as
        "no initializer provided". If you want to use None explicitly as the
        initializer, you can modify the function to use a unique sentinel.
    """

    # Validation: func must be callable
    if not callable(func):
        raise TypeError("Function must be callable")

    # Validation: iterable must be iterable
    try:
        iterator = iter(iterable)
    except TypeError:
        raise TypeError("Second argument must be iterable")

    # Initialize accumulator:
    # If initializer is provided (not None), start with it.
    # Otherwise use the first element of the iterable.
    if initializer is not None:
        acc = initializer
    else:
        try:
            acc = next(iterator)  # may raise StopIteration for empty iterable
        except StopIteration:
            # No initializer and empty iterable -> error (matches expected behavior)
            raise TypeError("reduce() of empty sequence with no initial value")

    # Reduction: apply func cumulatively left -> right
    for item in iterator:
        acc = func(acc, item)

    # Return final accumulated value
    return acc


# -------------------- Test Cases --------------------

# Test 1 - Basic numeric reduction (no initializer)
def add(a, b):
    return a + b

numbers = [1, 2, 3, 4, 5]
print(custom_reduce(add, numbers))  # Expected Output: 15


# Test 2 - With initializer (numeric)
def multiply(a, b):
    return a * b

nums = [2, 3, 4]
print(custom_reduce(multiply, nums, 10))  # Expected Output: 240


# Test 3 - String concatenation
def concat(a, b):
    return a + "-" + b

words = ["data", "science", "mastery"]
print(custom_reduce(concat, words))
# Expected Output: "data-science-mastery"


# Test 4 - Edge case: empty iterable with no initializer -> should raise TypeError
try:
    print(custom_reduce(lambda a, b: a + b, []))
except TypeError as e:
    print(e)  # Expected message: reduce() of empty sequence with no initial value


# Test 5 - Empty iterable with initializer provided
print(custom_reduce(lambda a, b: a + b, [], 0))  # Expected Output: 0


# -------------------- Reflection --------------------
print("How recursion or accumulation works step-by-step:")
print("1) An accumulator 'acc' holds the current result.")
print("2) If an initializer is provided, it becomes the starting 'acc'; otherwise")
print("   the first item of the iterable becomes 'acc'.")
print("3) For each next item, we compute acc = func(acc, item).")
print("4) After processing all items, 'acc' holds the final reduced result.")
print("This iterative accumulation avoids deep recursion and runs in O(n) time.")
