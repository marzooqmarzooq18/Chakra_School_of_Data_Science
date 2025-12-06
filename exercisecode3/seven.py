numbers = [4, -3, 7, -1, 0, -5, 9]

# Step 1: Count negative numbers
negative_count = 0

# Step 2: Replace negative numbers with zero
for i in range(len(numbers)):
    if numbers[i] < 0:
        negative_count += 1
        numbers[i] = 0

# Step 3: Print results
print("Count of negative numbers:", negative_count)
print("Updated list:", numbers)