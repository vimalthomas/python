import sys
#function for geenerator creation
def fun_generator(filename):
    for line in open(filename,'r'):
        yield line
#function for iterator creation
def fun_iterator(filename):
    f = open(filename,'r')
    return f


lst1 = fun_generator('data2.txt')
print(sys.getsizeof(lst1))
for i in lst1:
    print(i)
    print(sys.getsizeof(lst1))

lst2 = fun_iterator('data2.txt')
print(sys.getsizeof(lst2))
for i in lst2:
    print(i)
    print(sys.getsizeof(lst2))

#one liner for generator comprehension
lst3 = (line for line in open('data2.txt','r'))

for i in lst3:
    print(i)

#how to use generator without a loop and with stop iteraiton exception

lst4 = fun_generator('data2.txt')
print('generator through iterator exception block')
while True:
    try:
        i = next(lst4)
    except StopIteration:
        break
    print(i)
