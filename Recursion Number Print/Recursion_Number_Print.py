def recursion_number(n):
    '''
    n = Number

    recursion_number(n):
        Print each digit of "n" seperately using recursion.

    Example :
        n      = 123
        output = 1 2 3
    '''
    if n > 9:
        recursion_number(n//10)
    print(n % 10, end=" ")


if __name__ == "__main__":

    n = int(input('Enter the number = '))
    recursion_number(n)
