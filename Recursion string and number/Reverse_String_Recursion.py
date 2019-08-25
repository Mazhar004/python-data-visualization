def reverse_string(a,i=0):
    ''' String Reverse using recursion '''
    if i < len(a)-1:
        reverse_string(a,i+1)
    print(a[i],end="")
    
reverse_string('Hello World')