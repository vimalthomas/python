import time

#read throuhg regular open and file object

filename = "pseudo_facebook.csv"

t1 = time.time()
f = open(filename,"r")
lines = [line.rstrip("\n") for line in f ]
words = [word.split(",") for word in lines]
count = len(lines)
print('count of lines',count)
f.close()
t2 = time.time()
print('METHOD1:time taken',t2-t1)


#read with WITH Block and read method
t3 = time.time()
with open(filename) as infile:
    read_lines = infile.read()
    lines = read_lines.splitlines()
    words = [word.split(",") for word in lines]
    count = len(lines)
    print('count of lines',count)
t4 = time.time()
print('METHOD2:time taken',t4-t3)



# read with WITH and for loop (iterator)
t5 = time.time()
with open(filename) as infile:
    words=[]
    for line in infile:
        words.append(line.split(","))
    count=len(words)
    print('count of lines',count)
t6 = time.time()
print('METHOD3:time taken',t6-t5)



#read with a generator
t7=time.time()
f = open(filename,"r")
lines = (line.rstrip("\n") for line in f)
words = (word.split(",") for word in lines)
count=len(list(lines))
print('count of lines',count)
t8=time.time()
print('METHOD4:time taken',t8-t6)

#read with a readline chunk operator
t9=time.time()
bufsize = 600
with open(filename) as infile:
    count=0
    while True:
        lines = infile.readlines(bufsize)
        if not lines:
            break
        for line in lines:
            count+=1
#print(type(lines))
t10=time.time()
print('count of lines',count)
print('METHOD5:time taken',t10-t9)

#read lines with readlines method
t11=time.time()

with open(filename) as infile:
    count=0
    while True:
        lines = infile.readlines()
        if not lines:
            break
        for line in lines:
            count+=1
t12=time.time()
print('count of lines',count)
print('METHOD6:time taken',t12-t11)

#reading with line number and using tell and show
