
#this is my first script in python

#import all libraries
import random
import time

#list for random generator
ls = ['vimal','thomas','joseph','anandi','vellaiswamy','annvita','shanthi']

#function to create a dataset
def createdataset():
    num = 500000
    f = open('data.txt','w')
    for i in range(0,num):
        current = random.choice(ls)
        f.write(current+"\n")
    f.close()

def readdatasetls():
    countlist = []
    for i in ls:
        countlist.append(0)

    with open('data.txt','r') as f:
        for line in f:
            line = line.strip()
            if (line!=''):
                countlist[ls.index(line)]=countlist[ls.index(line)]+1




    print(countlist)

def readdatasetdct():
    countdict={}
    for i in ls:
        countdict[i]=0

    with open('data.txt','r') as f:
        for line in f:
            line = line.strip()
            if(line!=''):
                countdict[line]=countdict[line]+1


    print(countdict)

t1= time.time()
createdataset()
t2=time.time()
readdatasetls()
t3=time.time()
readdatasetdct()
t4=time.time()

print("time to create dataset",t2-t1)


print("time to count value using list",t3-t2)


print("time to count value using dict",t4-t3)
