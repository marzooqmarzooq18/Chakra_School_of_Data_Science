n = 4
size = 2 * n - 1

for i in range(size):
    for j in range(size):
        # Calculate the distance from each of the four borders:
        # 1. Distance from top border: i
        # 2. Distance from bottom border: size - 1 - i
        # 3. Distance from left border: j
        # 4. Distance from right border: size - 1 - j

        # Find the minimum distance to any border (min_dist)
        min_dist = min(i, j, size - 1 - i, size - 1 - j)

        # The number to be printed is n minus the minimum distance to the border.
        # This creates the concentric pattern.
        num = n - min_dist

        print(num, end=" ")

    print()