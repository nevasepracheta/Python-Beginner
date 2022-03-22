num1 =  float(input("Enter a number1: "))
num2 =  float(input("Enter a number2: "))

print("For addition; Type Add\nFor subtraction; Type Sub\nFor Multiplication; Type Prod\nFor Division; Type Div\n")
userinput = input("Enter your choice: ")
print(userinput)

if userinput.lower() ==  "add":
        print(num1 + num2)
elif userinput.lower() == "sub":
        print(num1 - num2)
elif userinput.lower() == "prod":
        print(num1*num2)
elif userinput.lower() == "div":
        print(num1//num2)
else:
        print("Invalid operation")
