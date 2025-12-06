n = 5  # you can change this value

for i in range(1, n + 1):
    # print leading spaces
    print(" " * (n - i), end="")

    # increasing numbers
    for j in range(1, i + 1):
        print(j, end="")

    # decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end="")

    # move to next line
    print()