from time import sleep


def progress_bar(value, maximum):
    '''
        def progress_bar(value, maximum):
            Will print progress bar for data loading status rescaling in percentage.
            
            value   = Value that will be loaded
            maximum = Maximum value for scaling
            
    '''
    value = int((value/maximum)*100)
    for i in range(1, value+1):
        sleep(.3)
        rightbar, leftbar, inchar, emptychar, width = "▌", " ▌", "█", '▬', 100
        fill_val = inchar*i
        empty_val = emptychar*(width-i)
        status = str(int((i/width)*100))
        if i == value:
            status += "%  Loaded"
        else:
            status += "% Loading"
        print(rightbar+fill_val+empty_val+leftbar+status, end="\r")
    print("\n")


if __name__ == '__main__':
    value, maximum = map(int, input("Input value & maximum = ").split(' '))
    print("\n")
    progress_bar(value, maximum)