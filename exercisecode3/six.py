numbers = [4, 15, 8, 21, 33, 2, 9, 14, 3, 7]

divisible_by_3 = []
even_and_greater_than_10 = []
odd_and_less_than_10 = []

for num in numbers:
    # Condition 1: Divisible by 3
    if num % 3 == 0:
        divisible_by_3.append(num)

    # Condition 2: Even and greater than 10
    if num % 2 == 0 and num > 10:
        even_and_greater_than_10.append(num)

    # Condition 3: Odd and less than 10
    if num % 2 != 0 and num < 10:
        odd_and_less_than_10.append(num)

print("Divisible by 3:", divisible_by_3)
print("Even and greater than 10:", even_and_greater_than_10)
print("Odd and less than 10:", odd_and_less_than_10)