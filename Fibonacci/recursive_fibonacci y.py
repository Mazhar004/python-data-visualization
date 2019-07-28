def fibonacci_recursion(count,previous=0,current=1):
    '''Here Previous and Current parameters are optional. So user did not need to input this value'''
    if count:
        print(previous,end=' ')
        fibonacci_recursion(count-1,current,previous+current)

        
        
n=int(input('Enter Number of Element for Fibonacci Series'))
fibonacci_recursion(n)