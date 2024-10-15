from random import randint
some_list = [randint(0, 100) for i in range(15)]
some_list_first_symbol = some_list[0]
some_list_last_symbol = some_list[-1]
some_list[0] = some_list_last_symbol
some_list[-1] = some_list_first_symbol