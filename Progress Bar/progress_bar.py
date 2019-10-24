from time import sleep


def progress_bar(value, maximum):
    value = int((value/maximum)*100)
    for i in range(1, value+1):
        sleep(.3)
        rightmost, leftmost, inchar, emptychar, width = "▌", " ▌", "█", '▬', 100
        print(rightmost+inchar*i+emptychar*(width-i) +
              leftmost+str(int((i/width)*100))+"%", end="\r")
    print("\n")


if __name__ == '__main__':
    value, maximum = map(int, input("Input value & maximum =").split(' '))
    progress_bar(value, maximum)
