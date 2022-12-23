def loadInput():
    file = open('day19/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def main():
    lines = loadInput()
    for i, line in enumerate(lines):
        print(line)


main()
