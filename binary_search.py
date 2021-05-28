
#you are given an array, len, low and high. implement a binary search_tree


def binary_search(arr,low,high,elem):

    mid = (low+high)//2
    #print('inside the function')
    if (high>=low):

        if(arr[mid]==elem):
            print("element found")
            #print(arr[mid],elem)
        elif(arr[mid]>elem):
            self.binary_search(self,arr,low,mid-1,elem)
            #print('inside mid>elem',arr[mid],elem)
        else:
            self.binary_search(self,arr,mid+1,high,elem)
            #print('inside mid<elem, array value',arr[mid],'elem',elem,'low',low,'high',high,'mid',mid)
    else:
        print('element doesnt exist')




ls = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6,6, 6, 6, 6, 6,6, 6, 6, 6, 6, 6,6, 6, 6, 6, 6, 6,6, 6, 6, 6, 6, 6,6, 6, 6, 6, 6, 6,6, 6, 6, 6, 6, 6]


#Get length, low and high

length = len(ls)
low = 0
high = length-1

binary_search(ls,low,high,44)
