# Given lists
lists = [  # A list containing three sub-lists
    [1, 2, 3, 4],  # The first sub-list (index 0)
    [2, 4, 6, 8],  # The second sub-list (index 1)
    [4, 2, 9, 10]  # The third sub-list (index 2)
]

# Empty list to store common numbers
common = []  # Initialize an empty list to collect numbers found in all three lists

# Loop through each number in the first list
for num in lists[0]:  # Iterate over every 'num' in the first sub-list (lists[0])

    # Check if the number is in the second and third list
    # The 'in' operator checks for membership in a list/collection
    if num in lists[1] and num in lists[2]:
        # Add to common list
        common.append(num)  # If the number is present in ALL three lists, add it to 'common'

# Print the result
print(common)  # Output the list of numbers common to all three lists