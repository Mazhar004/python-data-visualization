def reverse_string(string, i=0):
    '''
    String = Input string
    i      = It's an optional parameter for counting positioning.

    reverse_string(string, i=0):
        Print reversed string using recursion.

    Example:
        string = "Hello world"
        output = "dlrow olleh"
    '''
    if i < len(string)-1:
        reverse_string(string, i+1)
    print(string[i], end="")


if __name__ == "__main__":

    string = input('Enter the string = ')
    reverse_string(string)
