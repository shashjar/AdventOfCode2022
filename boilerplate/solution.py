def loadInput():
    file = open('day1/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def main():
    lines = loadInput()
    for line in lines:
        print(line)


main()