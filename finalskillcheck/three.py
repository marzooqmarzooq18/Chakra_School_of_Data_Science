def custom_filter(predicate, iterable) -> list:
    """
    Mimics Python’s built-in filter().
    Returns all elements for which predicate(element) is True.
    """

    # Step 1: Validate that predicate is callable
    if not callable(predicate):
        raise TypeError("Predicate must be a callable function")

    # Step 2: Create an empty list for results
    results = []

    # Step 3: Loop through each element in the iterable
    for item in iterable:
        # Step 4: Apply the predicate; if True, add to results
        if predicate(item):
            results.append(item)

    # Step 5: Return the final filtered list
    return results


# -------------------- Test Cases --------------------

# Example 1 - Numeric filtering
def is_even(n):
    return n % 2 == 0

print(custom_filter(is_even, [10, 15, 20, 25, 30]))
# Expected Output: [10, 20, 30]


# Example 2 - String filtering
def has_vowel(word):
    return any(ch in 'aeiou' for ch in word.lower())

words = ["sky", "apple", "rhythm", "echo", "fly"]
print(custom_filter(has_vowel, words))
# Expected Output: ['apple', 'echo']


# Example 3 - Error handling
try:
    print(custom_filter("not_callable", [1, 2, 3]))
except TypeError as e:
    print(e)
# Expected Output: TypeError: Predicate must be a callable function


# -------------------- Reflection --------------------
print("Why functional abstraction matters:")
print("Functional abstraction allows code to be reused with different logic by passing functions as arguments.")
print("It separates 'what to do' from 'how to do it', making code cleaner, flexible, and easier to maintain.")
