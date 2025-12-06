def make_pairs(students):
    pairs = []                   # empty list to store pairs
    for i in range(len(students)):       # outer loop
        for j in range(i+1, len(students)):  # inner loop, starts from i+1 to avoid repeats
            pairs.append((students[i], students[j]))  # add pair as a tuple
    return pairs


# Example usage
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
result = make_pairs(students)
print(result)