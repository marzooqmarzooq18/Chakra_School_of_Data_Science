# Example Sudoku grid input (partial)
grid = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
]

# Check if rows are valid
# This checks two things:
# 1. If the length of the row is equal to the number of unique elements in the row.
# 2. It also assumes, based on the context of a Sudoku check, that all numbers are between 1 and 9 and the length is 9.
# The len(row) == len(set(row)) part specifically checks for duplicates within the row.
valid_rows = all(len(row) == len(set(row)) for row in grid)

# Check if columns are valid
valid_columns = True
# Loop through each column index
for col in range(len(grid[0])):
    # Construct the column by taking the element at index 'col' from every row in the grid
    column = [grid[row][col] for row in range(len(grid))]

    # Check for duplicates in the column by comparing its length to the length of a set of its elements
    if len(column) != len(set(column)):  # If column has duplicates
        valid_columns = False
        break

# Final output
if valid_rows and valid_columns:
    print("Valid Sudoku rows and columns: True")
else:
    print("Valid Sudoku rows and columns: False")