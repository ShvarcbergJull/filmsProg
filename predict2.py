import sys
from sklearn import tree
import graphviz
import pickle

f=sys.stdin
lines=f.read().split("\n")
i = 0
j = 0


XARR = []
YARR = []

for line in lines:
    cols = line.split()
    if (cols):
        XARR.append([float(cols[0]), float(cols[1]), float(cols[2]), float(cols[3]), float(cols[4]), float(cols[5])])
        YARR.append(cols[6])
clf2 = tree.DecisionTreeClassifier(min_weight_fraction_leaf = 0.01, max_depth = 8)
clf2 = clf2.fit(XARR, YARR)

s=pickle.dumps(clf2)
ff=open("save_gone.dat","wb")
ff.write(s)
ff.close()

'''
for line in lines:
    cols=line.split()
    if (cols):
        EX = [cols[0], cols[1], cols[2], cols[3], cols[4], cols[5]]
        r2 = clf2.predict([EX])
        z1 = int(r2[0])
        if abs(z1 - int(cols[6]))<=200000000:
            j += 1
        print(str(cols[0])+' '+str(cols[1])+' '+str(cols[2])+' '+str(cols[3])+' '+str(cols[4])+' '+str(cols[5])+ ' ' + str(cols[6]) + ' ' + str(z1))
        i += 1
        
print(str(j/i))
'''