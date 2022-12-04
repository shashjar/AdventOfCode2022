def loadInput():
    file = open('day4/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def main():
    lines = loadInput()
    count = 0
    for line in lines:
        pair = line.split(",")
        firstElf = pair[0].split("-")
        secondElf = pair[1].split("-")

        firstElfStart = int(firstElf[0])
        firstElfEnd = int(firstElf[1])
        secondElfStart = int(secondElf[0])
        secondElfEnd = int(secondElf[1])

        if firstElfStart <= secondElfStart and secondElfEnd <= firstElfEnd:
            count += 1
        elif secondElfStart <= firstElfStart and firstElfEnd <= secondElfEnd:
            count += 1

    print(count)


main()
