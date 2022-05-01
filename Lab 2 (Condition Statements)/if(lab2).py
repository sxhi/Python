# Ray Sahi
# CIS 298
# If else, string manip, python basic+



# Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday. Write a program that asks a day number, and prints the day name (a string).
weekDays = [ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" ]
response = int(input("Please enter the day of the week (0-6): "))

looper = True
while (looper):
    if (int(response) >= 0 and int(response) < 7):
        print(weekDays[response])
        looper = False
        break
    else:
        response = int(input("Error! Number must be in between 0 and 7.\n"))


# Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the name of the day of the week you will return on.
weekDays = [ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" ]
response = int(input("Please enter the day of the week (0-6): "))
duration = int(input("Please enter the number of days till you return: "))
total = response + duration
calcDay = total % 7


if (int(response) >= 0 and int(response) < 7):
    print(weekDays[calcDay])
    
else:
    print("Error! Number must be in between 0 and 7.")


# Give the logical opposites of these conditions
# a) a > b
        # a <=b

# b) a >= b
        # a < b

# c) a >= 18 and day == 3
        # a < 18 or day != 3

# d) a >= 18 and day != 3
        # a < 18 or day == 3


# What do these expressions evaluate to?
print(3 == 3) # True
print(3 != 3) # False 
print(3 >= 4) # False
print(not (3 < 4)) # False


# Write a program which is given an exam mark, and it returns a string — the grade for that mark — according to this scheme:
numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
for i in range(len(numbers)):
    if (numbers[i] >= 75):
        print("First")
    elif (numbers[i] < 75 and numbers[i] >= 70):
        print("Upper Second")
    elif (numbers[i] < 60 and numbers[i] >= 65):
        print("Second")
    elif (numbers[i] < 60 and numbers[i] >= 50):
        print("Third")
    elif (numbers[i] < 50 and numbers[i] >= 45):
        print("F1 Supp")
    elif (numbers[i] < 45 and numbers[i] >= 40):
        print("F2")
    else:
        print("F3")


# Write a program which, given the length of two sides of a right-angled triangle, returns the length of the hypotenuse. (Hint: x ** 0.5 will return the square root.)
a = int(input("Please enter the length of side 1:"))
a = a ** 2
b = int(input("Please enter the length of side 2:"))
b = b ** 2
c = (a+b) ** 0.5
print("The final side is: ", c)


# Write a program which, given the length of three sides of a triangle, will determine whether the triangle is right-angled. 
# Assume that the third argument to the function is always the longest side. It will return True if the triangle is right-angled, or False otherwise.
a = float(input("Please enter the length of side 1:"))
a = a ** 2
b = float(input("Please enter the length of side 2:"))
b = b ** 2
c = float(input("Please enter the length of side 3:"))
c = c ** 2
x = a + b
y = c

threshold = 1e-7
if (abs(x-y) < threshold ):
    print("True")
else:
    print("False")

print(a + b == c)


# Extend the above program so that the sides can be given to the function in any order.
numbers = [0, 0, 0]
numbers[0] = float(input("Please enter the length of side 1:"))
a = numbers[0] ** 2
numbers[1] = float(input("Please enter the length of side 2:"))
b = numbers[1] ** 2
numbers[2] = float(input("Please enter the length of side 3:"))
c = numbers[2] ** 2
numbers.sort() #sort from least to greatest
x = numbers[0] + numbers[1]
y = numbers[2]

print(a + b == c)


# If you’re intrigued by why floating point arithmetic is sometimes inaccurate, on a piece of paper, divide 10 by 3 and write down the decimal result. 
# You’ll find it does not terminate, so you’ll need an infinitely long sheet of paper. 
# The representation of numbers in computer memory or on your calculator has similar problems: memory is finite, and some digits may have to be discarded. So small inaccuracies creep in.
import math
a = math.sqrt(2.0)
print (a, a*a)
print(a * a == 2.0)


# Write a program that prints We like Python's turtles! 1000 times.
turtles = str("We like Python's turtles!")
print(turtles * 1000)


# Assume you have the assignment numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# a)
for i in range(len(numbers)):
    print(numbers[i])

# b)
for i in range(len(numbers)):
    print(numbers[i], ", Squared: ", numbers[i] * numbers[i])

# c)
total = int(0)
for i in range(len(numbers)):
    total += numbers[i]
print("Total of all numbers: ", total)

# d)
mult = int(1)
for i in range(len(numbers)):
    mult *= numbers[i]
print("Product of all numbers: ", mult)


# Write a program to count how many odd numbers are in a list.
numbers = [5, 6, 7, 8, 9, 10]
count = int(0)
#find odds
for i in range(len(numbers)):
    if ((numbers[i] % 2) != 0):
        count += 1
print(count)


# Sum up all the even numbers in a list.
numbers = [5, 6, 7, 8, 9, 10]
count = int(0)
#find evens
for i in range(len(numbers)):
    if ((numbers[i] % 2) == 0):
        count += 1
print(count)


# Sum up all the negative numbers in a list.
numbers = [-5, -6, -7, 8, 9, 10]
count = int(0)

for i in range(len(numbers)):
    if (numbers[i] < 0):
        count += numbers[i]
print(count)


# Count how many words in a list have length 5.
numbers = ["Funny", "Lettuce", "Mahomeboy", "No", "Pondering", "Crazy"]
count = int(0)

for i in range(len(numbers)):
    if (len(numbers[i]) == 5):
        count += 1
print(count)


# Sum all the elements in a list up to but not including the first even number. (What if there is no even number?)
numbers = [3, 4, 6, 1, 7, 5]
count = int(0)

for i in range(len(numbers)):
    if (numbers[0] % 2 == 0):
        count = 0
    else:
        count += numbers[i]
print(count)


# Count how many words occur in a list up to and including the first occurrence of the word “sam”. (What if “sam” does not occur?)
numbers = ["sam", "likes", "apples"]
count = int(0)

for i in range(len(numbers)):
    if (numbers[i] == "sam"):
        count +=1
        print("sam has occured!")
        break
    else:
        count += 1
print(count)


# Add a print function to Newton’s sqrt algorithm that prints out better each time it is calculated. Call your modified program with 25 as an argument and record the results.
def sqrt(n):
    num = int(0)
    div = int(0)
    num = n/2
    div = (num + n/num)/2
    while div != num:
        num = div
        div = (num + n/num)/2
    print("better")
    return num

print(sqrt(25))
print(sqrt(25) + sqrt(100))


# Write a program that counts the number of even digits in n.
numbers = [5, 6, 8, 10, 12]
count = int(0)

for i in range(len(numbers)):
    if (numbers[i] % 2 == 0):
        count +=1
print(count)



