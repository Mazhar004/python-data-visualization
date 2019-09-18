def fibonacci(n):
    '''
        count = Number of value you want to print

        Example 1 : 
            count=3
            output= 0 1 1

        -----------------------

        Example 2 :
            count=6
            output= 0 1 1 2 3 5

    '''

    previous = 0
    current = 1
    for _ in range(n):
        print(previous, end=' ')
        previous, current = current, (previous+current)


if __name__ == "__main__":

    n = int(input('Enter Number of Element for Fibonacci Series = '))
    fibonacci(n)
