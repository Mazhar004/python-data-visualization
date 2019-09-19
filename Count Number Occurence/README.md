# Prime Number Occurence in Python3 #

## Description: ##

Every number can be represent as a multiplication of prime numbers.

## Program ##

* This function count the number of occurence of prime number "prime" in a given range "start" to "end"

  ``` 
  start = Starting Value
  end   = Ending Value
  prime = Prime Number
  ```
  ```
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
