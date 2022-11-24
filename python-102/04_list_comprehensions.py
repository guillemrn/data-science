numbers = []
for element in range(1, 11):
    numbers.append(element * 2)
print(numbers)

numbers_v2 = [element * 2 for element in range(1, 11)]
print(numbers_v2)

number_list = [i for i in range(20) if i % 2 == 0]
print(number_list)