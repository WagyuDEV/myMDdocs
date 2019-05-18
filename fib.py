def fib(counter):
    n1 = 0
    n2 = 1
    temp = None
    
    for x in range(0, counter):
        temp = n1
        n1 += n2
        n2 = temp
        print(n1)
        
fib(15)