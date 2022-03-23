try:
    number1 = int(input("Enter a number 1: "))
    number2 = int(input("Enter a number 2: "))
    print(number1//number2)

except ZeroDivisionError as err:
    print("Error Message: " + str(err))

except ValueError as err2:
    print("Error message: " + str(err))
