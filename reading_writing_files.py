employee_file = open("employees.txt", "r") # Open the external file
print(employee_file.readable()) # Using readable function to make sure your file is readable
#print(employee_file.readline()) # Here readline will print first line; readline() will read file line by line
#print(employee_file.readlines()) # readlines() will read all the line in the file and put the data in an array
#print(employee_file.readlines()[0])  # Using indexing we can accessing specific line in the file

for employee in employee_file:
    if "Accountant" in employee:
        print(employee)
    if "Salesperson" in employee:
        print(employee)
        
employee_file.close() # Closing the open file

employee_file = open("employees_IT.txt", "w") # Here we are creating a new file employees_IT.txt and writing to it.
# a for appending to existing file
# w will override the complete file is used directly. So when using w, create a new file
employee_file.write("\nKelly - IT")

employee_file.close()
