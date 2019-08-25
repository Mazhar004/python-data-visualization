def triangle(line):
    print('Its a triangle:')
    for i in range(1,line+1):
        print(' '*(line-i)+'*'*(2*i-1))


def right_triangle(line):
    print('Its a right triangle:')
    for i in range(1,line+1):
        print('*'*(2*i-1))


def square(line):
    if line<6:
        print('Try with a value greater than 5')
        return 0
    print('Its a square:')
    print('*'*line)
    for i in range(1,(line-2)//2):
        print('*'+' '*(line-2)+'*')
    print('*'*line)


def rectangle(value):
    if value<6:
        print('Try with a value greater than 5')
        return 0
    print('Its a rectangle:')
    print('*'*2*value)
    for i in range(1,(value)//2-1):
        print('*'+' '*(2*value-2)+'*')
    print('*'*2*value)


def crown(line):
    print('Its a crown:')
    for i in range(1,line+1):
        print('*'*(2*i-1)+' '*(2*line-(2*i-1))+' '*(line-i)+'*'*(2*i-1)+' '*(line-i)+' '*(2*line-(2*i-1))+'*'*(2*i-1))
    for i in range(1,line+1):
        print('*'*(2*line*3-1))
        

triangle(10)
right_triangle(10)
square(20)
rectangle(20)
crown(5)