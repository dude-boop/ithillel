import random
random_number = random.randint(3,6)
some_rand_list = []
for i in range(random_number):
    some_rand_list.append(random.randint(1,100))
new_list = []
print(some_rand_list)
for i in some_rand_list:
    if 0 == some_rand_list.index(i):
        new_list.append(i)
    elif 2 == some_rand_list.index(i):
        new_list.append(i)
new_list.append(some_rand_list[-2])
print(new_list)