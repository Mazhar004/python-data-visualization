def runner_up(a):
    a=list(map(int,a.split(' ')))
    first,second= (a[0],a[1]) if a[0]>a[1] else (a[1],a[0])
    for i in a[2:]:
        if i>first:
            first,second=i,first
        elif i>second:
            first,second=first,i
    print(first,second)
    
#a=input('Enter Number=')
a='1 3 4 2 56 7 8 23'
runner_up(a)