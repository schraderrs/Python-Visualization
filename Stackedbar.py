import numpy as np
import matplotlib.pyplot as plt
import csv

countMCM = 0
countTNW = 0
count3D = 0
countGD = 0
countMMR = 0
countMC = 0
countMO = 0
countMAS = 0
labels = 'The Next Web', 'Crossmedia', '3D', 'Gamedesign', 'Minor Multimediaal Reclamebureau', 'Minor Concepting', 'Minor Ondernemen', 'Minor Art \'n\' Sound'

with open('Minorenkeuze2.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
# Minoren: Crossmedia, Transmedia storytelling, The next web, 3D, gamedesign, multimediaal reclamebureau, concepting, ondernemen, art 'n sound, serious media
    for line in csv_reader:
        for item in line:
            if item == "Minor Crossmedia" or item == "Minor Transmedia Storytelling":
                countMCM += 1
            elif item == "Minor The Next Web":
                countTNW += 1
            elif item == "Minor 3D":
                count3D += 1
            elif item == "Minor Gamedesign" or item == "Minor Game Design":
                countGD += 1
            elif item == "Minor Multimediaal Reclamebureau":
                countMMR += 1
            elif item == "Minor Concepting": 
                countMC += 1
            elif item == "Minor Ondernemen":
                countMO += 1
            elif item == "Minor Art n Sound":
                countMAS += 1


print(countMCM, " ", count3D, " ", countGD, " ", countMMR, " ", countTNW, " ", countMC, " ", countMO, " ", countMAS)
sizes = [countTNW, countMCM, count3D, countGD, countMMR, countMC, countMO, countMAS]
explode = (0, 0, 0, 0, 0, 0, 0, 0.5)


fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')


# N = 2


# menMeans = (countTNW, countMCM)

# ind = np.arange(N)
# width = 0.35

# p1 = plt.bar(ind, menMeans, width, yerr=0)
# plt.ylabel('Aantal Studenten')
# plt.title('Aantal Studenten per Minor')
# plt.xticks(ind, ('TNW', 'MCM'))




plt.show()