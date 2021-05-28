
ls = [0, 88, 0, 63, 59, 0, 20, 10, 1]
write_index = len(ls)-1
print(ls)
cnt = ls.count(0)
for i in reversed(range(0,len(ls))):

    if(ls[i]!=0):
        ls[write_index]=ls[i]
        write_index-=1

print(ls)
print(cnt)
for i in range(0,cnt):
    ls[i]=0

print(ls)


#if 0 skip, else write
