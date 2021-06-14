
#program to find min and max index of a sorted list.
ls = [1, 1, 1, 2, 2, 2, 2, 2, 5,1,3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]

#sort the list, create a dictionary where keys are the unique elements and the index are the
#values


set_ls=set(ls)
#sort the list
#print(ls)
ls.sort()
#print(ls)

print(ls)
# first method using index and count method.
d={}
for i in set_ls:
    #index value
    #find the count
    #min is index value
    #max is count -1
    min_x = ls.index(i)
    max_x = (min_x+ls.count(i))-1
    d[i]=(min_x,max_x)

    print('min value of ',i,' is ',min_x)
    print('max value is ',i,'is',max_x)

print(d)

#second method
d={}
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
