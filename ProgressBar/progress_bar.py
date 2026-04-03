from time import sleep


def progress_bar(value, maximum):
    """Print a visual progress bar rescaled to percentage.

    Args:
        value: Current progress value.
        maximum: Maximum value for scaling.
    """
    percentage = int((value / maximum) * 100)

    right_bar = "\u258c"
    left_bar = " \u258c"
    fill_char = "\u2588"
    empty_char = "\u252c"
    width = 100

    for i in range(1, percentage + 1):
        sleep(0.3)
        filled = fill_char * i
        empty = empty_char * (width - i)
        status = f"{int((i / width) * 100)}%"
        status += "  Loaded" if i == percentage else " Loading"
        print(f"{right_bar}{filled}{empty}{left_bar}{status}", end="\r")

    print()


if __name__ == "__main__":
    value, maximum = map(int, input("Input value & maximum = ").split())
    print()
    progress_bar(value, maximum)
