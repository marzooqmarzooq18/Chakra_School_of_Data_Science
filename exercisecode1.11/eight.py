matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matrix)  # Get the number of rows (which is also the number of columns in a square matrix)

# Loop through each column index (0, 1, 2)
for col in range(n):

    # Loop through each row index in reverse order (n-1 down to 0)
    # This traverses the column from bottom to top
    for row in range(n - 1, -1, -1):
        # Print the element at [row][col]. 'end=" "' keeps the output on the same line,
        # followed by a space, for elements of the same column.
        print(matrix[row][col], end=" ")

    # After a column is printed, move to the next line for the next column's elements
    print()