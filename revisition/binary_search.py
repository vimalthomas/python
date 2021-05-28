class binary_search:
    def __init__(self,lst):
        self.length = len(lst)-1
        self.arr = lst



    def summary(self):
        return(self.length)

    def rev(self):
        new_ls = []
        new_ls = self.arr[::-1]
        return(new_ls)

    def new(self,elem):
        ar1 = self.arr
        arlength = self.length
        low = 0
        high=arlength

        self._bin_search(ar1,low,high,elem)
        #elif(ar1[mid])

    def _bin_search(self,ar1,low,high,elem):
        mid = (low+high)//2

        if(high>=low):
            if(ar1[mid]==elem):
                print('elem found')
            elif(ar1[mid]>elem):
                #print(ar1,low,mid-1,elem)
                self._bin_search(ar1,low,(mid-1),elem)

            elif(ar1[mid]<elem):
                #print(ar1,mid+1,high,elem)
                self._bin_search(ar1,(mid+1),high,elem)

        else:
            print('elem not found')

    def regular_search(self,elem):
        ar1 = self.arr
        if elem in (ar1):
            print('elem found')
        else:
            print('elem not found')

import time

lst = range(1,100000000000000000,1)

bin = binary_search(lst)

print('length calculated by class method is ',bin.summary())

reversed_ls = bin.rev()
print(bin.rev())
t1 = time.time()
bin.new(13)
t2 = time.time()
print('time taken',t2-t1)
t3 = time.time()
bin.regular_search(13)
t4 = time.time()
print('time taken',t4-t3)
