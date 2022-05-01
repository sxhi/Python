# Ray Sahi
# CIS 298
# Tuples



# Create an empty tuple and print the tuple
emptyTuple = ()
print(emptyTuple, '\n')

# Create a singleton tuple and print the tuple
singletonTuple = (63,)
print(singletonTuple, '\n')

# Create a tuple of 5 items of mixed types and print the tuple
mytuple = (1, 2, 'c', 'd', "hello")
print(mytuple, '\n')

# Print the 3rd item in the tuple, Print the item at index -3
print(mytuple[2], '\n')
print(mytuple[-3], '\n')

# Change the 3rd item in the tuple to “bye” and print the whole tuple, Change the -4th item in the tuple to ‘hello’ and print the whole tuple
# mytuple[2] = "bye"      # Tuples are immutable
# print(mytuple)

# Print the length of the tuple
print(len(mytuple), '\n')

# Find the min and max of the tuple
numTuple = (1, 2, 4, 10, 11, 12)
min = min(numTuple)
max = max(numTuple)
print("Min:", min, "\nMax:", max)

# Delete the -5th item in the tuple
# Tuple items cannot be deleted

# Add tuple [‘heaven’, -986] to the beginning of your tuple
mytuple = ('heaven', -986) + mytuple
print(mytuple, '\n')

# Append tuple [‘abc’,1,”ABC” ] to the end of your tuple
mytuple = mytuple + ('abc', 1, "ABC")
print(mytuple, '\n')

# Add ‘hello’ to the end of your tuple.  What happened?
mytuple = mytuple + ('hello', )
print(mytuple, '\n')

# Append “world” to the end of your tuple. What happened?
mytuple = mytuple + ("world", )
print(mytuple, '\n')

# Print your tuple, perform pop() on your tuple, and print the tuple again, Perform pop(4) on your tuple and print the tuple, Perform pop(-2) on your tuple and print the tuple
# print(mytuple, '\n')
# mytuple.pop()
# Cannot perform pop on tuple as values cannot be changed.

# Print the length of your tuple as a float
print("Length of Tuple:", len(mytuple))

# Print the type and ord of your tuple
print([type(item) for item in  mytuple])
#Ord cannot be performed as it can only work on sets of the same type, and not mixed. 