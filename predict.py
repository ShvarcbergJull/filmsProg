import pickle
from sklearn import tree
import sys

i = 0
j = 0
k = 0
f=sys.stdin

lines=f.read().split("\n")

ff=open("save_rat.dat","rb")
s2=ff.read()
ff.close()
clf1=pickle.loads(s2)

dciti = open("dictionary.dat", "r")
dic = {}
dac = []
for line in dciti:
    cols = line.split(';')
    if (cols):
        dic[cols[0]] = cols[1]

for line in lines:
    cols=line.split(',')
    if(cols):
        gun = cols[4].split('|')
        ex=[dic[cols[0]],dic[cols[1]],dic[cols[2]],dic[cols[3]],dic[gun[0]]]
        r1=clf1.predict([ex])
        z1=float(r1[0])
        dac.append(z1)

ff1=open("save_gone.dat","rb")
s3=ff1.read()
ff1.close()
clf2=pickle.loads(s3)

for line in lines:
    cols=line.split(',')
    if(cols):
        gun = cols[4].split('|')
        ex1=[dic[cols[0]],dic[cols[1]],dic[cols[2]],dic[cols[3]],dic[gun[0]], dac[i]]
        r=clf2.predict([ex1])
        z=float(r[0])
        if abs(z - int(cols[6]))<=200000000:
            j += 1
        if abs(z1 - float(cols[5]))<=1:
            k += 1
        print(cols[0] + ' ' + cols[1] + ' ' + cols[2] + ' ' + cols[3] + ' ' + cols[4] + ' ' + str(dac[i]) + ' ' + str(z))
        i += 1
print(k/i)
print(j/i)
