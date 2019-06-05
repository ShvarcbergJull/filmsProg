import sys
from sklearn import tree

i = 0
j = 0
f=sys.stdin
lines=f.read().split("\n")
file = open("films.dat", "r")
dirc = {}

for line in file:
    cols = line.split(";")
    if (cols):
        dirc[cols[0]] = cols[1]
        
for line in lines:
    cols = line.split(",")
    if (cols):
        #print(cols[1])
        #if (dirc.get(cols[1], 0) != 0):
        for name in dirc.keys():
            if cols[1] == name:
                print(str(cols[2]) + ',' + str(cols[3]) + ',' + str(cols[4]) + ',' + str(cols[5]) + ',' + str(cols[6]) + ',' + str(cols[7]) + ',' + str(dirc[cols[1]]))
                j += 1
                break
        i += 1