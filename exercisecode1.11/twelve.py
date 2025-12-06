n = 5

# Upper part
for i in range(1, n + 1):
    # This formula creates a butterfly-like pattern by printing:
    # 1. 'i' number of '*'
    # 2. '2 * (n - i)' number of spaces (which decreases as i increases)
    # 3. 'i' number of '*'
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

# Lower part (start at n-1 to avoid repeating the middle line)
for i in range(n - 1, 0, -1):
    # This is the reverse of the upper part, causing the pattern to close inward.
    print("*" * i + " " * (2 * (n - i)) + "*" * i)