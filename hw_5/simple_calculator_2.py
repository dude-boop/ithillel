
while True:
    x = input("Enter 'y' if you want to continue: ")
    if x == "y":
        num_1 = int(input("Enter your first number: "))
        num_2 = int(input("Enter your second number: "))
        answer = int(input("""
            Enter your type of operation: 
            1 2 3 4
            + - / *
            """))

        if answer == 1:
            print(num_1 + num_2)
        elif answer == 2:
            print(num_1 - num_2)
        elif answer == 3:
            if num_2 != 0:
                print(num_1 / num_2)
            else:
                print("division by zero, try another numbers")
        elif answer == 4:
            print(num_1 * num_2)
        else:
            print("Invalid input")
    else:
        print("Exit from calculator")
        break