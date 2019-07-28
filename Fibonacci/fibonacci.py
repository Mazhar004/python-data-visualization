def fibonacci(n):
    print('\n0',end=' ')
    previous=0
    current=1
    for i in range(n-1):
        print(current,end=' ')
        previous,current=current,(previous+current)
    print('\n')

n=int(input('Enter Number of Element for Fibonacci Series'))
fibonacci(n)