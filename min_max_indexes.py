
#you are given an array, len, low and high. implement a binary search_tree


def binary_search_min(arr,low,high,elem):

    mid = (low+high)//2
    #print('inside the function')
    if (low<=high):

        if(arr[mid]==elem and (high==low or mid==low)):
            print("min element found",low)
            print(high)
            print(arr[mid])
            print(low)
            #print(arr[mid],elem)
        elif(arr[mid]>=elem):
            print('inside mid>elem','array value',arr[mid],'elem',elem,'low',low,'high',high,'mid',mid)
            binary_search_min(arr,low,mid-1,elem)

            #print('inside mid>elem',arr[mid],elem)
        else:
            print('inside mid<elem, array value',arr[mid],'elem',elem,'low',low,'high',high,'mid',mid)
            binary_search_min(arr,mid+1,high,elem)
            #print('inside mid<elem, array value',arr[mid],'elem',elem,'low',low,'high',high,'mid',mid)
    else:
        print('element doesnt exist')


def binary_search_max(arr,low,high,elem):

    mid = (low+high)//2
    #print('inside the function')
    if (low<=high):

        if(arr[mid]==elem ):
            print("max element found",low,high)
            print(high)
            print(arr[mid])
            print(low)
            #print(arr[mid],elem)
        elif(arr[mid]>=elem):
            print('inside mid>elem','array value',arr[mid],'elem',elem,'low',low,'high',high,'mid',mid)
            binary_search_max(arr,low,mid-1,elem)

            #print('inside mid>elem',arr[mid],elem)
        else:
            print('inside mid<elem, array value',arr[mid],'elem',elem,'low',low,'high',high,'mid',mid)
            binary_search_max(arr,mid+1,high,elem)
            #print('inside mid<elem, array value',arr[mid],'elem',elem,'low',low,'high',high,'mid',mid)
    else:
        print('element doesnt exist')


ls = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6,6, 6, 6, 6, 6,6, 6, 6, 6, 6, 6,6, 6, 6, 6, 6, 6,6, 6, 6, 6, 6, 6,6, 6, 6, 6, 6, 6,6, 6, 6, 6, 6, 6]


#Get length, low and high

length = len(ls)
low = 0
high = length-1

binary_search_min(ls,low,high,1)

binary_search_max(ls,low,high,1)
