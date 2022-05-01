# Ray Sahi
# CIS 298
# Timer

import math
import time

def isEvens(x):
    temp = x
    while temp > 0:
        if temp%2 == 1:                   
            return False                   
        temp = math.floor(temp / 10)      
    return True                      

evens = []
start = time.time()
for i in range(1000, 3001):              
    if isEvens(i):              
        evens.append(i)
end = time.time()
print(evens)
sum = end - start
print("Total time taken:", end - start)

evens2 = []
start = time.time()
for i in range(1000, 3001):              
    if isEvens(i):              
        evens2.append(i)
end = time.time()
print(evens2)
sum2 = end - start
print("Total time taken:", end - start)

evens3 = []
start = time.time()
for i in range(1000, 3001):              
    if isEvens(i):              
        evens3.append(i)
end = time.time()
print(evens3)
sum3 = end - start
print("Total time taken:", end - start)

avg = (sum + sum2 + sum3) / 3
print("The average of the times is: ", avg)



# Ray Sahi
# CIS 298

import time
import math
import decimal
import functools
import itertools
import operator

def findCombo(key, increment):

    numbers = (decimal.Decimal(i) * increment for i in range(1, 712))
    testNums = (i for i in numbers if (key * (1 / increment ** 4) % i) == 0)

    combos = itertools.combinations(testNums, 4)
    
    for nums in combos:
        if (key == functools.reduce(operator.add, nums) and key == functools.reduce(operator.mul, nums)):
            combo = list(nums)
    print(combo)

key = decimal.Decimal('7.11')
inc = decimal.Decimal('0.01')
start = time.time()
findCombo(key, inc)
finish = time.time() - start
print("This code ran in %s seconds.\n" %(finish))


def FindNumber():
    for w in range(0, 711):
        for x in range(0, 711 - w):
            for y in range(0, 711 - w - x):
                z = 711 - x - y - w
                if (w * x * y * z == 711000000):
                    return w,x,y,z
start_time = time.time()
w,x,y,z = FindNumber()
print(w/100 ,x/100,y/100,z/100) 
print("--- %s seconds ---" % (time.time() - start_time))
