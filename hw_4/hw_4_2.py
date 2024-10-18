some_list = []
if some_list != []:
    counter = 0
    for i in range(0, len(some_list)):
        if i % 2 == 0:
            counter += some_list[i]
    counter *= some_list[-1]
else:
    print("Your list is empty")