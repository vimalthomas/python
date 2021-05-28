
sen='hello world, this is me'

word = sen.split(" ")
res=[]
for i in (word):
    for j in reversed(i):
        res.append(j)
    res.append(" ")
print(*res)
