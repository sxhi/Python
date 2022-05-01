# Ray Sahi
# CIS 298
# Intro



# Take the sentence: All work and no play makes Jack a dull boy. Store each word in a separate variable, then print out the sentence on one line using print.
a = "All "
b = "work "
c = "and "
d = "no " 
e = "play "
f = "makes "
g = "Jack "
h = "a "
i = "dull "
j = "boy."
print(a + b + c + d + e + f + g + h + i + j)


# Add parenthesis to the expression 6 * 1 - 2 to change its value from 4 to -6.
a = (6 * (1 - 2))
print(a)


# Start the Python interpreter and enter bruce + 4 at the prompt. This will give you an error. Assign a value to bruce so that bruce + 4 evaluates to 10.
bruce = 6
print(bruce + 4)


# Write a program that replaces these letters with something a bit more human-readable, 
# and calculate the interest for some varying amounts of money at realistic interest rates such as 1%, and -0.05%. When you have that working, 
# ask the user for the value of some of these variables and do the calculation.
print("Welcome to the Compound Interest Calculator!")
principal = int(input("Enter Principal Amount: "))
rate = float(input("Enter Interest Rate: "))
num = int(input("Enter the number of times it is compounded per year: "))
time = int(input("Enter the number of years: "))
total = principal * ( ( 1 + (rate / num) ) ** (num * time) )
print("The final amount after ", time, " years is: ", total)


# What happened with the last example? Why? If you were able to correctly anticipate the computer’s response in all but the last one, it is time to move on.
a = 5%2 #should evaluate to 1
b = 9%5 #should evaluate to 4
c = 15%12 #should evaluate to 3
d = 12%15 #should evaluate to 12
e = 6%6 #should evaluate to 0
f = 0%7 #should evaluate to 0
g = 7%0 #should be undefined, cant divide by zero
print(a, " ", b, " ", c, " ", d, " ", e, " ", f, " ", g)


# You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours. At what time does the alarm go off?
hours = 5100
time = 1400
finaltime = (1400 + 5100) % 2400
print(finaltime)


# Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours), and ask for the number of hours to wait. 
# Your program should output what the time will be on the clock when the alarm goes off.
currentTime = int(input("Enter the current time: "))
isPm = int(input("If PM, enter 1: "))
alarm = int(input("Enter the number of hours: "))

if (isPm == 1):
	currentTime += 12

days = alarm % 24
currentTime += days

if (currentTime >= 24):
	currentTime -= 24

elif (currentTime == 0):
	print("12AM")

elif (currentTime == 12):
	print("12PM")

elif (currentTime > 12):
	print(currentTime-12, "PM")

else:
	print(currentTime, "AM")

