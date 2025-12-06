def spiral_order(matrix):
    """
    Performs spiral traversal on a given matrix of any size.
    """
    if not matrix or not matrix[0]:
        return []

    # Initialize boundaries dynamically based on the input matrix size
    top = 0
    bottom = len(matrix) - 1  # Max row index (total rows - 1)
    left = 0
    right = len(matrix[0]) - 1  # Max column index (total columns - 1)

    spiral = []

    while top <= bottom and left <= right:

        # Step 1: Move -> (left to right) along the 'top' row
        for j in range(left, right + 1):
            spiral.append(matrix[top][j])
        top += 1

        # Check if boundaries have crossed (e.g., in a single-row matrix)
        if top > bottom:
            break

        # Step 2: Move ↓ (top to bottom) along the 'right' column
        for i in range(top, bottom + 1):
            spiral.append(matrix[i][right])
        right -= 1

        # Check if boundaries have crossed (e.g., in a single-column matrix)
        if left > right:
            break

        # Step 3: Move <- (right to left) along the 'bottom' row
        # This is performed only if there are still rows left to traverse
        for j in range(right, left - 1, -1):
            spiral.append(matrix[bottom][j])
        bottom -= 1

        # Check if boundaries have crossed
        if top > bottom:
            break

        # Step 4: Move ↑ (bottom to top) along the 'left' column
        # This is performed only if there are still columns left to traverse
        for i in range(bottom, top - 1, -1):
            spiral.append(matrix[i][left])
        left += 1

    return spiral


# --- Examples of usage with different size matrices ---

# 1. Your original 4x4 matrix
matrix_4x4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
print(f"4x4 Spiral: {spiral_order(matrix_4x4)}")
# Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

# 2. A 3x5 matrix (more columns than rows)
matrix_3x5 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]
print(f"3x5 Spiral: {spiral_order(matrix_3x5)}")
# Output: [1, 2, 3, 4, 5, 10, 15, 14, 13, 12, 11, 6, 7, 8, 9]

# 3. A 5x3 matrix (more rows than columns)
matrix_5x3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
]
print(f"5x3 Spiral: {spiral_order(matrix_5x3)}")
# Output: [1, 2, 3, 6, 9, 12, 15, 14, 13, 10, 7, 4, 5, 8, 11]

# 4. A single-row matrix
matrix_1x4 = [[1, 2, 3, 4]]
print(f"1x4 Spiral: {spiral_order(matrix_1x4)}")
# Output: [1, 2, 3, 4]