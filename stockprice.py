


def profit(list):
    d = {}
    for i in range(0,len(list)):
        #print(i)
        for j in range(i+1,len(list)):
            #print('the buying price is ',list[i],'selling price',list[j],'profit',list[j]-list[i])
            d[(list[i],list[j])]=list[j]-list[i]

            #print("break")
    max_profit = max(d.values())
    #print(max_profit)
    for i,k in d.items():
        if (k==max_profit):
            print("best buying and selling  price combiantion",i,"best profit",max_profit)


l1 = [8,5,12,9,19,1]
l2 = [21,12,11,9,6,3]
l3 = [1, 2, 3, 4, 3, 2, 1, 2, 5]
l4 = [8, 6, 5, 4, 3, 2, 1]
profit(l1)
#print('new list \n')
profit(l2)
profit(l3)
profit(l4)
