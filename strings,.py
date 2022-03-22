# STRINGS
character_name = "Tom"  # String variable, written inside " "
character_age = 13  # Numeric value in the string be written directly
is_male = True  # String can also hold Boolean value
#print("Name of the protagonist is " + character_name + ".")
#print("His age is " + str(character_age) + ".")
# While using number string, you will have to convert it to str if concatenating  with other strings
#character_name = "Mike"  # Reassigning same variable
#print("His friend is " + character_name)

pharse = "Giraffe Academy"
print(pharse.lower() + " is cool")  # String concatenation; using lower() to print str in lowercase.
print(pharse.upper())  # Using upper() convert str to uppercase
print(pharse.isupper())  # Checking if str is in all uppercase
print(pharse.upper().isupper()) # Combination is functions
print(len(pharse)) # Pass the variable inside len() to length of the str

#Accessing characters in the string
print(pharse[0]) # Indexing starts with 0
print(pharse.index("a")) # index() returns index of the element in str

print(pharse.replace("Giraffe","Elephant")) # Replace str within str
