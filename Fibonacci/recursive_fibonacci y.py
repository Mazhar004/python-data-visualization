def fibonacci_recursion(count, previous=0, current=1):
    '''
        count = Number of value you want to print

        fibonacci(count, previous=0, current=1):

            Here previous & current parameters are optional. So user don't need to input this value.

            This function return fibonacci series, which has n number of digit.

        Example 1 : 
            count  = 3
            output = 0 1 1

        -----------------------

        Example 2 :
            count  = 6
            output = 0 1 1 2 3 5
    '''
    if count:
        print(previous, end=' ')
        fibonacci_recursion(count-1, current, previous+current)


if __name__ == "__main__":

    n = int(input('Enter number of element for fibonacci series = '))
    fibonacci_recursion(n)
