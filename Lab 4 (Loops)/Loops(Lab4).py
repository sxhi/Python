# Ray Sahi
# CIS 298
# Conditonal Statements and Loops



# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
for i in range(1500, 2700):
    if ((i % 7 == 0) and (i%5 == 0)):
        print(i)


# Write a Python program to convert temperatures to and from celsius, fahrenheit.  Formulas : F = 9C / 5+32 or C = (f-32)* 5 / 9
loop_control = True

while loop_control:
    try:
        user = int(input("Which measurement are you using? (1 for Fahrenheit, 2 for Celsius), press '0' to quit.\n"))
        
        if( (user != 1) and (user != 2) and (user != 0) ):
           raise ValueError('Input must be either 0, 1, 2')
        
        if (user== 0):
            print("Thanks for using the temperature conversion")
            loop_control = False

        if (user == 1):
            conversion = int(input("Please enter the temperature in Fahrenheit:"))
            celsius = float(((conversion - 32) * (5/9)))
            print(conversion, "F is " , celsius, "C.\n")

        if (user == 2):
            conversion = int(input("Please enter the temperature in Celsius:"))
            fahrenheit = float(((9 * conversion) / (5)) + 32)
            print(conversion, "C is " , fahrenheit, "F.\n")

    except ValueError as excpt_val:
        print(excpt_val)
        print("Please correct your input\n")


# Write a Python program to guess a number between 1 to 9
import random
correctNum = random.randint(1,9)
isCorrect = False

while isCorrect != True:
    guess = int(input("Take a guess 1-9\n"))
    try:
        if ( (guess < 1) or (guess > 9) ):
            raise ValueError("Guess must be between 1-9")
        
        elif (guess == correctNum):
            print("WOW! You got the correct answer of ", correctNum, "!")
            isCorrect = True
    except ValueError as err_val:
        print("Please fix input.\n")


# Write a Python program to construct the following pattern, using a nested for loop.
for i in range(10):
    if (i <= 4):
        for j in range (i+1):
            print('*', end = '')
    else:
        for j in range(10 - i-1):
            print('*', end = '')
    print()



# Write a Python program to get the Fibonacci series between 0 to 50.
first = 0
buff = 1
while buff <= 50:
    print(buff, end = "\n")
    temp = buff
    buff = first+buff
    first = temp


# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
for i in range (6):
    if ( (i % 3 != 0) or (i == 0) ):
        print(i, "\n")


# Write a Python program to count the number of even and odd numbers from a series of numbers.
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
countE = 0
countO = 0

for i in numbers:
    if not i % 2:
        countE += 1
    else: 
        countO += 1

print("Number of Evens: ", countE)
print("\nNumber of Odds:", countO)


# Write a Python program that prints each item and its corresponding type from the following list.
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, -12], {'class' : 'V', 'section' : 'A'}]
for i in datalist:
    print("The type of", i, "is", type(i))


# Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1, 50):
    if ((i % 3 == 0) and (i % 5 == 0)):
        print('FizzBuzz')
    elif(i % 3 == 0):
        print('Fizz')
    elif(i % 5 == 0):
        print('Buzz')
    print(i)


# Write a Python program that accepts a string and calculate the number of digits and letters.
digits = 0
letters = 0
word = input("Please enter anything: ")
for i in word:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        letters += 1

print("The number of letters in", word, "is", letters, "\n The number of digits in", word, "is", digits)


# Write a Python program to check whether an alphabet is a vowel or consonant.
vowels = ['A','E','I','O','U']
choice = input("Please input a letter:  ")
if choice.upper() in vowels:
    print(choice, "is a vowel.")
else:
    print(choice, "is a consonant")


# Write a Python program to check a string represent an integer or not. 
choice = input("Enter a string: ")
if(choice.isdigit()):
    print(choice, "is an integer")
else:
    print(choice, "is a String")


# Re-Write problem 10 as a function that returns the count of letters, digits, and other.
def counter(word):
    digits = 0
    letters = 0
    for i in word:
        if i.isdigit():
            digits += 1
        elif i.isalpha():
            letters += 1
    print("The number of letters in", word, "is", letters, "\n The number of digits in", word, "is", digits)

    
word = input("Please enter anything: ")
counter(word)



# Write a function that returns two values: first is a Boolean of whether or not the passed-in string value is a float number. Second is the float value of the string or -1.0 if not a float.
def isFloat(choice):
    for i in choice:
        if i.isdigit():
            print(True)
            return True
        elif i.isAlpha():
            return i
        else:
            print(-1.0)
            return -1.0

choice = input("Please input anything:  ")
isFloat(choice)


# Write a function to calculate tips. It should have two parameters, one for total amount and one for tip percentage to use. Make the default percentage 15%, using default parameter value.
def calcTip(total, tip):
    if (tip == 0):
        tip == 15;
        temp = total * (tip/100)
        total = total + temp
        print("The total is", total)
    else:
        temp = total * (tip/100)
        total = total + temp
        print("The total is", total)
total = float(input("Please enter the total cost:  "))
tip = float(input("Please enter the tip percentage:  "))
calcTip(total, tip)