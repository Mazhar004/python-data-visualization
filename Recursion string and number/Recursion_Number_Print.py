def recursion_number(a):
    '''Print each digit in a number seperately using recursion'''
    if a>9:
        reverse_number(a//10)
    print(a%10,end=" ")

reverse_number(1234)
