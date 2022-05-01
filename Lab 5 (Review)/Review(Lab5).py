# Ray Sahi
# CIS 298
# Review


# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array (list containing lists). The element value in the i-th row and j-th column of the array should be i*j.
import csv
x = int(input("How many rows? "))
y = int(input("How many columns? "))
table = []
for i in range(x):
    temp = []
    for j in range(y):
        temp.append(i*j)
    table.append(temp)
print(table)

# Write to file
with open("output.txt", "w+") as file1:
    for item in table:
        file1.write("%s\n" %item)
file1.close()

# Read from file
with open("output.txt", "r") as file3:
    content = file3.read()
print(content)
file3.close()

# Write to file in binary  (Incorrect)
with open("output.bin", "wb") as file2:
    for item in table:
        bytes = bytearray(cobs(delta_rows[item].getByte_List()))
        file2.write(bytes)
file2.close()

# Read from file in binary   (Incorrect)
with open ("output.bin", "rb") as file4:
    content = file4.read()
print(content)
file4.close()

# Write to CSV file
with open('output.csv', 'w+', newline = '') as file6:
    csvcontent = csv.writer(file6)
    csvcontent.writerows(table)
file6.close()

# Read from CSV file
with open('output.csv', 'r', newline = '') as file7:
    csvcontent = csv.reader(file7)
    for row in csvcontent:
        print(row)
file7.close()


# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
sample = input("Please enter a string: ")
words = sample.split(',')
words.sort()
print(words)


# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
sample = input("Please enter a string: ")
words = sample.split(' ')
words.sort()
print(words)


# Write a program that accepts a sentence and calculate the number of uppercase letters and lowercase letters.
sample = input("Please enter a string: ")
upper = 0
lower = 0
for letters in sample:
    if letters.islower():
        lower = lower + 1
    elif letters.isupper():
        upper = upper + 1
print("The string '%s' has %d lowercase letters and %d uppercase letters." %(sample, lower, upper))


# Print only odd numbers from a list of integers
sample = list(map(int,input().split(',')))
result = [print(num) for num in sample if num%2==1]


# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
sample = input("Enter a string: ")
sample = sample.split(' ')
A = dict()

for word in sample:
    if word not in A:
        A[word] = 1
    elif word in A:
        A[word] += 1

for (key, value) in sorted(A.items()):
    print(key, ":", value)


# Create a dictionary with telephone country prefixes and country name
C = dict(USA = "United States of America", ARG = "Argentina", BRA = "Brazil", CHN = "China", IND = "India", ISR = "Israel", ITA = 'Italy')
print(C, '\n')


# Write a program that contains multiple nested dictionaries.  The first dictionary has key of city name. 
# The inner dictionary contains sport as key.  The next inner dictionary contains team name, #wins, #losses.  Display for every team, its win percentage (wins / (wins+losses)). 
# Find the city that has the highest combined average winning percentage from all of its teams (add winning percentage of each team in city and divide by number of teams).

cities = { "Detroit" : { "C-Football" : { "Wolverines": "Michigan", "Wins": 13 , "Losses": 0},
                          "Football" : { "Lions": "Detroit", "Wins": 8 , "Losses": 9},
                          "Basketball" : { "Pistons": "Detroit", "Wins": 52 , "Losses": 30}
    
                        },
       "Los Angeles" : { "C-Football" : { "Trojans": "Southern California", "Wins": 10 , "Losses": 3},
                          "Football" : { "Rams": "Los Angeles", "Wins": 12 , "Losses": 5},
                          "Basketball" : { "Lakers": "Los Angeles", "Wins": 61 , "Losses": 19}
    
                        }    
}
print(cities)
winningpct = 0.0
cityname = ""
for x in cities:
    count = 0
    sum = 0.0
    for y in cities[x]:
        per=float(cities[x][y]['Wins'])/float(cities[x][y]['Wins']+cities[x][y]['Losses'])
        print(x, cities[x][y], per)
        count = count + 1
        sum = sum + per
    avg = sum / count
    if ( winningpct < avg ):
        winningpct = avg
        cityname = x
print(cityname)    


# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. 
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
sample = input("Please enter a binary number:").split(',')

result = []
for x in range(len(sample)):
    if (int(sample[x], 2) % 5 == 0):
        result.append(sample[x])
print(result)


# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
import math

def isEvens(x):
    temp = x
    while temp > 0:
        if temp%2 == 1:                   
            return False                   
        temp = math.floor(temp / 10)      
    return True                      

evens = []
for i in range(1000, 3001):              
    if isEvens(i):              
        evens.append(i)
print(evens)


# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
def check(password):
   if not (len(password) >= 6 and len(password) <= 12):
       return False
   check1=0
   check2=0
   check3=0
   check4=0

   for letters in password:
       num=ord(i)
       if num<=90 and num>=65:
           check3+=1
       elif num>=97 and num<=122:
           check1+=1
       elif num<=57 and num>=48:
           check2+=2
       elif i in '$#@':
           check4+=1
       else:
           return False
   if check1*check2*check3*check4!=0:
       return True
   return False


passwords=input().split(',')
ans = ""
for password in passwords:
    if check(password):
        ans += password + ","
        print(ans.rstrip(','))


# Practice with the basic string methods:
sample = "whats good in The 313"
print(sample.isalpha(), '\n')
print(sample.islower(), '\n')
print(sample.isupper(), '\n')
print(sample.isdigit(), '\n')
print(sample.startswith('w'), '\n')
print(sample.endswith('3'), '\n')
print(sample.lower(), '\n')
print(sample.upper(), '\n')
print(sample.title(), '\n')
print(sample.lstrip(), '\n')
print(sample.rstrip(), '\n')
print(sample.strip(), '\n')
print(sample.ljust(5), '\n')
print(sample.rjust(5), '\n')
print(sample.center(5), '\n')
print(ord('%'))

sample2 = 'delicious'
print(sample2[0])
print(sample2[-1])
print(sample2[1])
print(sample2[-2])
print(sample2[:5])
print(sample2[6:])
print(sample2[2:5])
print(sample2[-1:])
print(sample2[:-1]) 

print('^'*36)
print("Hello World!"*5)
multi = '''LeBron is still the Goat and 
Everyone who thinks Michael Jordan would win 8 straight finals
is absolutely DELUSIONAL!'''
print(multi)
print("Length:",len(multi))

phonenum = '1-800-555-1212'
print(phonenum.replace('1-800','1 (800)').replace('-555-',' 555.'))
Quote = "These are the times that try men's souls"
for word in Quote.split():
    print(word)
print(Quote[20:])


Date = '02/14/2019'
date = Date.split('/')
day = date[0]
month = date[1]
year = date[-1]
print(year + "/" + month + "/" + day)