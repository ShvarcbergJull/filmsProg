import sys
from sklearn import tree
import graphviz
import pickle

f=sys.stdin
lines=f.read().split("\n")
i = 0
j = 0
XARR1 = []
YARR1 = []

for line in lines:
    cols=line.split()
    if (cols):
        XARR1.append([float(cols[0]), float(cols[1]), float(cols[2]), float(cols[3]), float(cols[4])])
        YARR1.append(cols[5])
clf1 = tree.DecisionTreeClassifier(min_weight_fraction_leaf = 0.01, max_depth = 8)
clf1 = clf1.fit(XARR1, YARR1)

s=pickle.dumps(clf1)
ff=open("save_rat.dat","wb")
ff.write(s)
ff.close()

'''
for line in lines:
    cols=line.split()
    if (cols):
        EX = [cols[0], cols[1], cols[2], cols[3], cols[4]]
        r1 = clf1.predict([EX])
        z = float(r1[0])
        if abs(z - float(cols[5]))<=1:
            j += 1
        print(str(cols[0])+' '+str(cols[1])+' '+str(cols[2])+' '+str(cols[3])+' '+str(cols[4])+' '+str(cols[5])+' '+str(z))
        i += 1
       
print(str(j/i))
'''