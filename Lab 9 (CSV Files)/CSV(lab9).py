# Ray Sahi
# CIS 298
# Scores Program

import csv
import statistics
import sys
import math

printstd = sys.stdout
filename = "scores.csv"
DQFile = open('DQ.txt', 'w+')
scores = dict()
highestScore = 0
highestScoredPlayer = ''
lowestScore = 100
lowestScoredPlayer = ''

with open("scores.csv") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        # Maps all at 2 and beyond to a list, converting to int.
        scoreslist = list(map(lambda x: int(x), line[2:]))
        name = line[1] + ' ' + line[0]

        if -1 in scoreslist:
            DQplayers = [str(x+1) for x in range(0, len(scoreslist)) if scoreslist[x] == -1] 
            sys.stdout = DQFile
            print(name, "didn't participate in round(s):", ",".join(DQplayers))
        scores[name] = scoreslist

sys.stdout.close()
DQFile.close()
sys.stdout = printstd

players = dict()

for player in scores:
    if scores[player] == -1:
        scores[player] = 0
        playerTotal = sum(scores[player])
        players[player] = playerTotal
    if scores[player] == 0:
        scores[player] = -1
    playerTotal = sum(scores[player])

    if highestScore < playerTotal:
        highestScore = playerTotal
        highestScorePlayer = player

    if lowestScore > playerTotal:
        lowestScore = playerTotal
        lowestScorePlayer = player

print('Highest Total:', highestScorePlayer, "@", highestScore)
print('Lowest Total:', lowestScorePlayer, "@", lowestScore)

outfile = open('ScoresOut.txt', 'w+')
sys.stdout = outfile
print({k: v for k, v in sorted(players.items(), key=lambda item: item[1], reverse = True)}) 
sys.stdout.close()
sys.stdout = printstd
outfile.close()


print('Qualification Rounds:')
validPlayers = {k:v for (k,v) in scores.items() if not -1 in v}

totalValidScores = []
for player in validPlayers:
    totalValidScores.append(sum(scores[player]))

print("Mean of all Qualified Participants: ", round(statistics.mean(totalValidScores), 1))
print("Median of all Qualified Participants: ", round(statistics.median(totalValidScores)), 1)

rounds = []
for x in range(0, 4):
    for score in scores:
        rounds.append(scores[score][x])
    validScores = [i for i in rounds if i != -1]
    print("ROUND", x+1, ': Average =', round(statistics.mean(validScores), 1))
