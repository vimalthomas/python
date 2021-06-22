#add the previous two numbers and output

def fibo(max_count):

    first = 0
    second = 1
    result = first + second

    while(result<=max_count):
        result = first + second
        first = second
        second = result
        if(result>max_count):
            return
        print(result)



fibo(10000)
