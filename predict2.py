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
