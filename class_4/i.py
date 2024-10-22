# import random
#
# NUM_SIZE = random.randint(3, 6)
# numbers = []
#
# for i in range(NUM_SIZE):
#     numbers.append(random.randint(1, 100))
# print(numbers)

numbers = [3, 1, 4, 2, 5]
print(numbers)
max_value = max(numbers)
min_value = min(numbers)

maximum_index = numbers.index(max_value)
minimum_index = numbers.index(min_value)

numbers[maximum_index] = min_value
numbers[minimum_index] = max_value

print(numbers)