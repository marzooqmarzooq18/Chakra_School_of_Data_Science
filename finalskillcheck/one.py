def find_most_frequent(data_list: list) -> list:
    """
    Find the most frequent element(s) in a list without using collections.Counter.

    Args:
        data_list (list): The input list containing elements (numbers, strings, etc.)

    Returns:
        list: Sorted list of element(s) that occur most frequently.
    """

    # Step 1: Create a dictionary to store frequency of each element
    freq = {}

    # Step 2: Count occurrences manually
    for item in data_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    # Step 3: Find the maximum frequency
    max_freq = max(freq.values())

    # Step 4: Collect all elements having that maximum frequency
    most_frequent = [key for key, value in freq.items() if value == max_freq]

    # Step 5: Sort elements safely (ignore incomparable types)
    try:
        most_frequent.sort()
    except TypeError:
        # Ignore sorting errors if mixed data types (e.g., int and str)
        pass

    return most_frequent


# -------------------- Test Cases --------------------

# Example 1
data_list1 = [3, 1, 3, 2, 1, 3, 1, 1, 2]
print(find_most_frequent(data_list1))  # Expected Output: [1]

# Example 2
data_list2 = ["apple", "mango", "apple", "banana", "banana", "mango"]
print(find_most_frequent(data_list2))  # Expected Output: ['apple', 'banana', 'mango']

# -------------------- Reflection --------------------
print("How I optimized without Counter:")
print("I used a dictionary to count each element’s frequency in one pass (O(n) time).")
print("Then I found the maximum frequency and filtered items having that value.")
print("This avoided importing Counter while keeping the logic clear and efficient.")
