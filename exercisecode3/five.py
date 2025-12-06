numbers = [1, 2, 3, 4, 5]

new_list = []

for num in numbers:
    if num % 2 == 0:
        new_list.append(num * 2)  # Multiply even number by 2
    else:
        new_list.append(num ** 2) # Square the odd number

print("Original list:", numbers)
print("New list:", new_list)