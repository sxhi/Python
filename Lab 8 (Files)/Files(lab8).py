#################Q1

# Ray Sahi
# CIS 298
# Files

import matplotlib.pyplot as plt
import numpy as np

filename = "input.txt"
fileHandler = open(filename, 'r')
varMap =  dict(a = 0, b = 0, c = 0, d = 0, e = 0, f = 0, g = 0, h = 0, i = 0, j = 0, k = 0, l = 0, m = 0, n = 0, o = 0, p = 0, q = 0, r = 0, s = 0, t = 0, u = 0, v = 0, w = 0, x = 0, y = 0, z = 0)



for char in fileHandler.read():
    char = char.lower()
    if char.isalpha():
        if char in varMap.keys():
            varMap[char] += 1
    elif char.isnumeric():
        if str(char) in varMap.keys():
            varMap[str(char)] += 1
        else:
            varMap[str(char)] = 1

for key in sorted(varMap.keys()):
    print(key, ":", varMap[key])

x = list(sorted(varMap.keys()))
y = list(varMap.values())
plt.bar(range(len(varMap)), y, tick_label=x)
plt.title("Bar Graph of Course Syllabus")
plt.xlabel("Characters: ")
plt.ylabel("Frequency: ")
plt.show()



################### Q2
# Ray Sahi
# CIS 298
# Files

import matplotlib.pyplot as plt
import re

filename = "Frankenstein.txt"
fileHandler = open(filename, 'r')
varMap = dict()

for line in fileHandler:

    words = line.split(" ")
    
    for word in words:
        word = word.lower()
        for char in word:
                if char == "!" or char == "." or char == "?":
                     if char in varMap:
                        if len(char) != 0:
                            varMap[char] += 1 
                            word = word.replace(char, "")
                     else:
                        if len(char) != 0:
                            varMap[char] = 1
                            word = word.replace(char, "")

                elif char == "-" or char == "," or char == "(" or char == " " or  char == ")" or char == "[" or char == "]" or char == "{" or char == "}"  or char == "*" or char == '"' or char == '%' or char == '$' or char == ";" or char == ":" or char == "/" or char == "'" or char == "_":
                    word = word.replace(char, "")
        
        if len(word) != 0:
            word = re.sub(r'[^\w\']', '', word)
            if word in varMap:
                varMap[word] += 1
            else:
                varMap[word] = 1


#Sorted dict by frequency ascending order
ascMap = {k: v for k, v in sorted(varMap.items(), key = lambda item: item[1], reverse = True)}

for key in sorted(list(varMap.keys())):
    print(key, ":  Frequency: ", varMap[key])

words = list(ascMap.keys())[:50]
frequency = [ascMap[words[i]] for i in range(50)]


# 50 Most Used Words
plt.bar(range(len(words)), frequency)
plt.title("50 Most Used Words:")
plt.xticks(range(len(words)), words, rotation = 90)
plt.xlabel("Words:")
plt.ylabel("Frequency: ")
plt.show()


words = list(varMap.keys())
words = sorted(words, key = len, reverse = True)
longest = words[:50]
longest = sorted(longest, key = len)
frequency = [varMap[longest[i]] for i in range(50)]

# 50 Longest Words
plt.bar(range(len(longest)), frequency)
plt.title("50 Longest Words:")
plt.xticks(range(len(longest)), longest, rotation = 90)
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.show()