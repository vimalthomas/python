
ls = [0, 88, 0, 63, 59, 0, 20, 10, 1]

output = [0,0,0,88, 63, 59, 20, 10, 1]

#i thin can use a iterator

ls_iter = iter(ls)
ls_output = []
#if 0 skip, else write

while True:
    try:
        i = next(ls_iter)
        if(i!=0):
            ls_output.append(i)
    except StopIteration:
        break
count_range = ls.count(0)

for i in range(0,count_range):
    ls_output.insert(i,0)
print(ls_output)
