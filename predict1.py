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
