fruits = ["apple", "banana", "cherry", "mango", "grape"]
print(fruits[0])
print(fruits[-1])
print(fruits[-2])



fruits = ["apple", "banana", "cherry", "berry"]
print(fruits[0])
print(fruits[1])
print(fruits[3])



fruits = ["apple", "banana", "cherry", "mango", "grape"]
print(fruits[1:]) # This prints a slice starting from index 1 to the end



fruits = ["apple", "banana", "cherry", "mango", "grape"]
# This slice starts at index 5 (which is out of bounds for a 5-element list)
# and has a step of -1. In Python, an out-of-bounds start index for a slice
# often results in an empty list.
print(fruits[5::-1])


numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print("Sum of numbers:", total)