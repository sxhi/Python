# Ray Sahi
# CIS 298
# Final Exam Q

import matplotlib.pyplot as plt
import pandas as pd

word_dict = {'a' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             'b' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             'c' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             'd' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             'e' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             'f' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             'g' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             'h' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             'i' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             'j' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             'k' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             'l' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             'm' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             'n' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             'o' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             'p' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             'q' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             'r' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             's' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             't' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             'u' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             'v' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             'w' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             'x' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             'y' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },
             'z' : {'total' : 0, 'pos1' : 0, 'pos2' : 0, 'pos3' : 0, 'pos4' : 0, 'pos5' : 0 },}

with open("answers.txt", 'r') as filehandler:
    for line in filehandler:
        words = line.split(" ")
        for word in words:
            count = -1
            word = word.lower()
            for char in word:
                count += 1
                if char.isalpha():
                    if char in word_dict:
                        word_dict[char]['total'] += 1
                    if count == 0:
                        word_dict[char]['pos1'] += 1
                    elif count == 1:
                        word_dict[char]['pos2'] += 1
                    elif count == 2:
                        word_dict[char]['pos3'] += 1
                    elif count == 3:
                        word_dict[char]['pos4'] += 1
                    elif count == 4:
                        word_dict[char]['pos5'] += 1

print(word_dict)

sorted_total = {}
sorted_pos1 = {}
sorted_pos2 = {}
sorted_pos3 = {}
sorted_pos4 = {}
sorted_pos5 = {}

# Undoing Nested Dict
for id, info in word_dict.items():
    for key in info:
        if key == 'total':
            sorted_total[id] = info[key]
        elif key == 'pos1':
            sorted_pos1[id] = info[key]
        elif key == 'pos2':
            sorted_pos2[id] = info[key]
        elif key == 'pos3':
            sorted_pos3[id] = info[key]
        elif key == 'pos4':
            sorted_pos4[id] = info[key]
        elif key == 'pos5':
            sorted_pos5[id] = info[key]

total = {k: v for k, v in sorted(sorted_total.items(), key = lambda item: item[1], reverse = True)}
position1 = {k: v for k, v in sorted(sorted_pos1.items(), key = lambda item: item[1], reverse = True)}
position2 = {k: v for k, v in sorted(sorted_pos2.items(), key = lambda item: item[1], reverse = True)}
position3 = {k: v for k, v in sorted(sorted_pos2.items(), key = lambda item: item[1], reverse = True)}
position4 = {k: v for k, v in sorted(sorted_pos2.items(), key = lambda item: item[1], reverse = True)}
position5 = {k: v for k, v in sorted(sorted_pos2.items(), key = lambda item: item[1], reverse = True)}


# Grouped Bar Chart (FINAL EXAM QUESTION)
pd.DataFrame(word_dict).T.plot(kind = 'bar')
plt.xlabel("Alphabet")
plt.ylabel("Frequency")
plt.title("Grouped Bar Chart")
plt.legend(loc = 'upper right')
plt.show()


# Total
plt.bar(total.keys(), total.values())
plt.title("Total Frequencies:")
plt.xlabel("Alphabet")
plt.ylabel("Frequency")
plt.show()

# Position 1
plt.plot(position1.keys(), position1.values())
plt.title("Position 1 Frequencies:")
plt.xlabel("Alphabet")
plt.ylabel("Frequency")
plt.show()

# Position 2
plt.plot(position2.keys(), position2.values())
plt.title("Position 2 Frequencies:")
plt.xlabel("Alphabet")
plt.ylabel("Frequency")
plt.show()

# Position 3
plt.plot(position3.keys(), position3.values())
plt.title("Position 3 Frequencies:")
plt.xlabel("Alphabet")
plt.ylabel("Frequency")
plt.show()

# Position 4
plt.plot(position4.keys(), position4.values())
plt.title("Position 4 Frequencies:")
plt.xlabel("Alphabet")
plt.ylabel("Frequency")
plt.show()

# Position 5
plt.plot(position5.keys(), position5.values())
plt.title("Position 5 Frequencies:")
plt.xlabel("Alphabet")
plt.ylabel("Frequency")
plt.show()

# Totals Graph
inner_keys = list(word_dict.values())[0].keys()
xvals = list(map(str, word_dict.keys()))

for x in inner_keys:
    yvals = [v[x] for v in word_dict.values()]
    line1, = plt.plot(xvals, yvals, label = x)
    plt.legend()
plt.xlabel("Alphabet")
plt.ylabel("Frequency")
plt.show()
