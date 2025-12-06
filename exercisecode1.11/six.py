# Matrix (2D list)
matrix = [ # Define the 2D list (matrix) containing the numbers
    [1, 2, 3], # First row
    [4, 5, 6], # Second row
    [7, 8, 9]  # Third row
] # End of the matrix

# Row sum calculation
print("Row sums:") # Print a header for the row sums
for row in matrix: # Start a loop to iterate through each 'row' in the 'matrix'
    total = 0 # Initialize a variable 'total' to 0 for the current row sum
    for num in row: # Start an inner loop to iterate through each 'num' (number) in the current 'row'
        total += num # Add the current 'num' to the running 'total'
    print(total) # Print the final 'total' sum for the current row

# Column sum calculation
print("Column sums:") # Print a header for the column sums
for col in range(3): # Start a loop to iterate through column indices (0, 1, 2) since there are 3 columns
    total = 0 # Initialize a variable 'total' to 0 for the current column sum
    for row in matrix: # Start an inner loop to iterate through each 'row' in the 'matrix'
        total += row[col] # Access the element at the current 'col' index of the 'row' and add it to 'total'
    print(total) # Print the final 'total' sum for the current column