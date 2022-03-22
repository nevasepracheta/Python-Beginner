lucky_numbers = [4, 54, 6, 23, 12, 78, 44]
friends = ["Kev", "Andy", "Jim", "Pam", "Oscar", "Angela", "Jim", "Jim"]  # Declaration
friends_2 = ["Michael", "Phyllis"]
print(friends[0])  # First element in the list
print(friends[-1])  # Last element in the list

print(friends[1:])  # Pulls up all the elements starting from index 1
print(friends[1:3])  # Pulls up all the element between 1 and (3-1) index

friends[3] = "Dwight"  # Modifying element in the list
friends.extend(friends_2)  # Adding two list, elements of list passed to extend() will be added to the end
friends.append("Creed")  # Append to the existing list, always added at the end using append()
friends.insert(1, "Kelly")  # Insert element at the given index
print(friends)
friends.remove("Oscar")
friends.pop()
print(friends)
print(friends.count("Jim"))  # Counts the number of occurence of given element in the list
friends.remove("Jim")  # Removes first occurrence of a repeating element
print(friends)
friends.reverse() # Reverse the list alphabetically(if strings) and ascending(if numbers) order
print(friends)
lucky_numbers.reverse()
print(lucky_numbers)
office = friends.copy() # Copies existing list to new list
print(office)
