def runner_up(n):
    '''
    n= List of numbers

    runner_up(n):
        This function print value of first & second highest from the numbers list "n" .

    Example 1 :

    n= 1 3 4 2 56 7 8 23

    output 56 23
    '''
    n = [int(i) for i in n.split(' ')]
    first, second = (n[0], n[1]) if n[0] > n[1] else (n[1], n[0])
    for i in n[2:]:
        if i > first:
            first, second = i, first
        elif i > second:
            first, second = first, i
    print(first, second)


if __name__ == "__main__":

    #n = input('Enter space seperated numbers = ')
    n = '1 3 4 2 56 7 8 23'
    runner_up(n)
