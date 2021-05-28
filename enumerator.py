

ls = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]

d = {}

for i in (set(ls)):
    l=[]
    for x,y in enumerate(ls):
        if (y==i):
            l.append(x)
    d[i] = l
print(d)
for a,b in d.items():
    print(a)
    print('min index is ',min(b))
    print('max index is ',max(b))
