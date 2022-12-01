numbers = [1, 2, 3, 4, 5]
numbers_v2 = []
for number in numbers:
  numbers_v2.append(number * 2)

print(numbers)
print(numbers_v2)

numbers_v3 = list(map(lambda number: number * 2, numbers))
print(numbers_v3)


numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8, 9, 10]

print(numbers_1)
print(numbers_2)

result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)