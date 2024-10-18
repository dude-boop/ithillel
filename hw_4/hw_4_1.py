some_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
counter = some_list.count(0)
for i in range(counter):
        some_list.remove(0)
        some_list.append(0)
print(some_list)
