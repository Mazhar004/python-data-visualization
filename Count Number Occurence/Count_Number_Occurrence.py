def check(start, end, prime):
    '''
        start = Starting Value
        end   = Ending Value
        prime = Prime Number

        Check function count the number of occurence of prime number "prime" in a given range "start" to "end"

        Example 1:

        start = 1
        end   = 10
        prime = 2
                             Occurence of 2
        1     = 1                  0
        2     = 1*2                1
        3     = 1*3                0
        4     = 1*2*2              2
        5     = 1*5                0
        6     = 1*2*3              1
        7     = 1*7                0
        8     = 1*2*2*2            3
        9     = 1*3*3              0
        10    = 1*2*5              1

        Total =                    8

        ------------------------------

        Example 2:

        start = 1
        end   = 10
        prime = 3
                             Occurence of 3
        1     = 1                  0
        2     = 1*2                0
        3     = 1*3                1
        4     = 1*2*2              0
        5     = 1*5                0
        6     = 1*2*3              1
        7     = 1*7                0
        8     = 1*2*2*2            0
        9     = 1*3*3              2
        10    = 1*2*5              0

        Total =                    4
    '''
    count = 0
    for i in range(start, end+1):
        while True:
            if i % prime == 0:
                count += 1
                i /= prime
            else:
                break
    return '{} exist in between {}-{} = {} time'.format(prime, start, end, count)


if __name__ == "__main__":
    print(check(1, 10, 2))
    print(check(1, 10, 3))
