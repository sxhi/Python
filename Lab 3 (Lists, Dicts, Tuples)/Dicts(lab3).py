# Ray Sahi
# CIS 298
# Dict {}



# Build a dictionary with 6 college & mascot associations, using all three methods A = { key : value, key : value }, A = dict( [(key, value), (key,value)] ), A=dict( key=value, key=value )
A = {"UofM" : "Wolverines", "MSU" : "Spartans", "OSU" : "Buckeyes", "PSU" : "Nittany Lions", "USC" : "Trojans", "UofO" : "Ducks" }
B = dict([("UofM", "Wolverines"), ("MSU", "Spartans"), ("OSU", "Buckeyes"), ("PSU", "Nittany Lions"), ("USC", "Trojans"), ("UofO", "Ducks")])
C = dict(UofM = "Wolverines", MSU = "Spartans", OSU = "Buckeyes", PSU = "Nittany Lions", USC = "Trojans", UofO = "Ducks")
print("Method 1:\n", A, "\nMethod 2:\n", B, "\nMethod 3:\n", C, '\n')

# Access the dictionary using a key that doesn’t exist
print(A["UofM"], "\n") # print(A["TSU"]) Using an invalid key throws an error

# Add a new value to the dictionary and print the dictionary
C["CLEM"] = "Tigers"
print(C, '\n')

# Change the value of an existing entry and print the dictionary
C["MSU"] = "Trashcans"
print(C, '\n')

# Del an entry from the dictionary
del C["OSU"]
print(C, '\n')

# Check to see if a value is ‘in’ the dictionary and also ‘not in’ the dictionary
if ("UofM" in C.keys()):
    print("Go blue!")
if("OSU" not in C.keys()):
    print("Anyone missing? I dont think so.\n")

# Get the length of the dictionary
print("Length of Dictionary A:", len(A), "\nLength of Dictionary B:", len(B), "\nLength of Dictionary C:", len(C), "\n")

# Print a list of sorted keys to the dictionary
for key in sorted(C.keys()):
    print(key, ":", C[key])
