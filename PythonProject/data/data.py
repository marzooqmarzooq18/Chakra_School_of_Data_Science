fruits = ["apple", "banana", "cherry", "berry"]
print(fruits[0])
print(fruits[1])
print(fruits[3])
print(fruits[-1])
print(type(fruits))

fruits.append("Pomegranate")
print(fruits)

fruits.extend(["Kiwi", "Sapota"])
print(fruits)



for i in range(5):
 if i==3:
  continue
print(i)

i=11
while i<23:
  i+=1
  if i == 13:
   continue
  print(i)


  items = [1, 2, 2, 3, 4, 4, 5, 1]

  unique_items = []

  for item in items:
      if item not in unique_items:
          unique_items.append(item)

  print(unique_items)