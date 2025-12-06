# The initial list of integers
numbers = [5, 12, 7, 18, 9, 4, 13, 6, 1]

# Initialize the two new lists
even_gt_10 = []
odd_le_10 = []

# Loop through each number in the list
for num in numbers:
    # Check for the first condition: Even and greater than 10
    # A number is even if (num % 2) == 0
    if (num % 2 == 0) and (num > 10):
        even_gt_10.append(num)

    # Check for the second condition: Odd and less than or equal to 10
    # A number is odd if (num % 2) != 0 or (num % 2) == 1
    elif (num % 2 != 0) and (num <= 10):
        odd_le_10.append(num)

# Print the results as requested
print("Even numbers :", even_gt_10)
print("Odd numbers :", odd_le_10)