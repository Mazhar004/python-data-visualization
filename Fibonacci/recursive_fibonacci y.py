def fibonacci_recursion(count, previous=0, current=1):
    '''
        Here Previous and Current parameters are optional. So user did not need to input this value

        count = Number of value you want to print

        Example 1 : 
            count=3
            output= 0 1 1

        -----------------------

        Example 2 :
            count=6
            output= 0 1 1 2 3 5

    '''
    if count:
        print(previous, end=' ')
        fibonacci_recursion(count-1, current, previous+current)


if __name__ == "__main__":

    n = int(input('Enter Number of Element for Fibonacci Series = '))
    fibonacci_recursion(n)
