import sys
from sklearn import tree

f=sys.stdin
lines=f.read().split("\n")
i = 0
j = 0
act = 0

XARR1 = []
YARR1 = []
dic = {}

out = ""

for line in lines:
    cols=line.split(",")
    genr = cols[4].split("|")
    if (cols):
        for n in range(4):
            out += (str(dic.setdefault(cols[n], i)) + ' ')
            if dic[cols[n]] == i:
                i += 1
        out += (str(dic.setdefault(genr[0], i)) + ' ')
        if dic[genr[0]] == i:
            i += 1
        out += (str(cols[5]) + ' ' + str(cols[6]))
        #print(str(dic.setdefault(cols[1], i)) + ' ' + str(dic.setdefault(cols[2], i)) + ' ' + str(dic.setdefault(cols[3], i)) + ' ' + str(dic.setdefault(cols[4], i)) + ' ' + str(dic.setdefault(cols[5], i)) + ' ' + str(cols[6]) + ' ' + str(cols[7]))
        print(out)
        out = ""
        
file = open("dictionary.dat", "w")

for key in dic.keys():
    file.write(str(key) + ';' + str(dic[key]) + ' \n')