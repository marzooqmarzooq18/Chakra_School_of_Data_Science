nums = [-1, 0, 1, 2, -1, -4]  # The input list of numbers
n = len(nums)  # Get the length of the list

# Outer loop: iterates through the first element of the triplet
for i in range(n):

    # Second loop: iterates through the second element. It starts from i+1
    # to ensure j is always greater than i (avoiding duplicates and self-reference)
    for j in range(i + 1, n):

        # Third loop: iterates through the third element. It starts from j+1
        # to ensure k is always greater than j (avoiding duplicates)
        for k in range(j + 1, n):

            # Check if the sum of the three elements equals zero
            if nums[i] + nums[j] + nums[k] == 0:
                # If the sum is zero, print the triplet found
                # Note: This is a brute-force O(n^3) solution and will print duplicates
                # if the original list contains duplicate numbers that form a valid triplet.
                print([nums[i], nums[j], nums[k]])