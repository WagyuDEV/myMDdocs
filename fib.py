def fib(counter):
    n1 = 0
    n2 = 1
    temp = None
    
    for x in range(0, counter):
        temp = n1
        n1 += n2
        n2 = temp
        print(n1)
        
# fib(15) 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610
