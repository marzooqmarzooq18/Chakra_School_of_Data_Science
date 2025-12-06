def partition(arr: list, low: int, high: int) -> int:
    """
    Partitions the list around a pivot element.
    Elements smaller than pivot are moved to its left,
    and greater ones to its right.
    Returns the index of the pivot after partitioning.
    """
    pivot = arr[high]  # choosing last element as pivot
    i = low - 1        # pointer for smaller elements

    for j in range(low, high):
        if arr[j] <= pivot:  # move smaller element to left side
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # place pivot at correct sorted position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr: list, low: int = 0, high: int = None) -> None:
    """
    Sorts 'arr' in place using the Quick Sort algorithm.
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Partition the list and get pivot index
        pi = partition(arr, low, high)

        # Recursively sort elements before and after pivot
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# -------------------- Test Cases --------------------

# Example 1 – Basic numeric list
nums1 = [5, 2, 9, 1, 5, 6]
quick_sort(nums1)
print("Sorted:", nums1)  # Expected: [1, 2, 5, 5, 6, 9]

# Example 2 – Reverse sorted input
nums2 = [10, 9, 8, 7, 6]
quick_sort(nums2)
print("Sorted:", nums2)  # Expected: [6, 7, 8, 9, 10]

# Example 3 – Floats
nums3 = [3.2, 1.1, 4.8, 2.6]
quick_sort(nums3)
print("Sorted:", nums3)  # Expected: [1.1, 2.6, 3.2, 4.8]


# -------------------- Reflection --------------------
print("\nHow pivot choice impacts recursion depth and time complexity:")
print("Quick Sort divides the list around a pivot so that smaller values go left and larger go right.")
print("If the pivot is well-chosen (near the middle value), recursion depth stays low and runs in O(n log n).")
print("If the pivot is poor (like smallest or largest repeatedly in sorted input), it causes deeper recursion and can reach O(n²).")
