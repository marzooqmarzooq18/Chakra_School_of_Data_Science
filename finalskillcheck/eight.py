def merge_sort(arr: list) -> list:
    """
    Recursively sorts a list using the Merge Sort algorithm.
    Returns a new sorted list without modifying the original.
    """
    # Base Case: if list has 0 or 1 element, return as is
    if len(arr) <= 1:
        return arr

    # Divide: find the midpoint and split the list
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Conquer: recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Combine: merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left: list, right: list) -> list:
    """
    Merges two sorted lists into one sorted list (stable merge).
    """
    merged = []
    i = j = 0

    # Compare and merge elements from both lists
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # Stability: use <=
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append remaining elements from either list
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


# -------------------- Test Cases --------------------

# Example 1 – Basic numeric list
nums1 = [5, 2, 8, 1, 3]
print("Original:", nums1)
print("Sorted:", merge_sort(nums1))  # Expected: [1, 2, 3, 5, 8]

# Example 2 – Duplicate handling
nums2 = [4, 2, 4, 1, 3]
print("\nOriginal:", nums2)
print("Sorted:", merge_sort(nums2))  # Expected: [1, 2, 3, 4, 4]

# Example 3 – Floats
nums3 = [3.5, 1.2, 2.8]
print("\nOriginal:", nums3)
print("Sorted:", merge_sort(nums3))  # Expected: [1.2, 2.8, 3.5]


# -------------------- Reflection --------------------
print("\nHow divide-and-conquer achieves O(n log n) efficiency:")
print("Merge Sort repeatedly divides the list into smaller halves until single elements remain.")
print("Then, it merges those sorted parts together efficiently in linear time per level.")
print("Since the list is halved log(n) times and merged n times overall, the total time complexity is O(n log n).")
