def fun(a,b):
    return a**b


l1 = [2,3,4]
l2 = [2,3,4]

result = map(fun,l1,l2)
print(list(result))
