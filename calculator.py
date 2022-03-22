num1 =  input("Enter a number1: ")
num2 =  input("Enter a number2: ")

print("For addition; Type Add\nFor subtraction; Type Sub\nFor Multiplication; Type Prod\nFor Division; Type Div\n")
userinput = input("Enter your choice: ")
print(userinput)

if userinput.lower() ==  "add":
        print(float(num1) + float(num2))
elif userinput.lower() == "sub":
        print(float(num1) - float(num2))
elif userinput.lower() == "prod":
        print(float(num1)*float(num2))
elif userinput.lower() == "div":
        print(float(num1) // float(num2))
else:
        print("Invalid operation")
