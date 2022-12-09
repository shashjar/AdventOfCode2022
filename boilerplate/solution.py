def loadInput():
    file = open('day1/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def main():
    lines = loadInput()
    for i, line in enumerate(lines):
        print(line)


main()
