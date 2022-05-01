# Ray Sahi
# CIS 298
# Lists



# Empty List
emptyList = []
print(emptyList, '\n')

# Singleton List
singletonList = ['a']
print(singletonList, '\n')

# Five Items List
fiveitemList = ['a', 'b', 'c', 'd', 'e']
print(fiveitemList, '\n')

# Print the 3rd item in the list
print(fiveitemList[2], '\n')

# Print the item at index -3
print(fiveitemList[-3], '\n')

# Change the 3rd item in the list to "bye" and print the whole list
fiveitemList[2] = "bye"
print(fiveitemList, '\n')

# Change the 3rd item in the list to 'hello' and print the whole list
fiveitemList[-3] = 'hello'
print(fiveitemList, '\n')

# Print the length of the list
print("The length of the list is:", len(fiveitemList))

# Find the min and max of the list
min = min(fiveitemList)
max = max(fiveitemList)
print("\nMin:", min, "\nMax:", max)

# Delete the -5th item in the list
fiveitemList.remove(fiveitemList[-5])
print('\n', fiveitemList, '\n')

# Add list [‘heaven’, -986] to the beginning of your list
fiveitemList.insert(0, ['heaven', -986])
print(fiveitemList, '\n')

# Append list [‘abc’,1,”ABC” ] to the end of your list
fiveitemList.append(['abc', 1, "ABC"])
print(fiveitemList, '\n')

# Add ‘hello’ to the end of your list.  What happened?
fiveitemList.append('hello')
print(fiveitemList, '\n')

# Append “world” to the end of your list. What happened?
fiveitemList.append("world")
print(fiveitemList, '\n')

# Print your list, perform pop() on your list, and print the list again
print(fiveitemList, '\n')
fiveitemList.pop()
print(fiveitemList, '\n')

# Perform pop(4) on your list and print the list
fiveitemList.pop(4)
print(fiveitemList, '\n')

# Perform pop(-2) on your list and print the list
fiveitemList.pop(-2)
print(fiveitemList, '\n')

# Print the length of your list as a float
list_length = float(len(fiveitemList))
print(list_length, '\n')

# Print the type and ord of your list
print([type(item) for item in fiveitemList], '\n')
print(ord(fiveitemList))

