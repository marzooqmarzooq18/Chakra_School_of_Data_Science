list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
target = 10

for x in list1:
    for y in list2:
        if x + y == target:
            print((x, y))