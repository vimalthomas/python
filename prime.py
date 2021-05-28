
def prime(n):

    if(n<2):
        return False

    #for i in range(2,n-1):
    for i in range(2,int(n**(1/2))+1):
        #print(i)
        if(n%i==0):
            return False
    else:
        return True



#int((15**(1/2)))

for i in range(0,1000):
    if (prime(i)):
        print('the number',i,'is prime')
