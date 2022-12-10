def loadInput():
    file = open('day10/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def cycleNewLine(currCycle):
    return currCycle in [40, 80, 120, 160, 200, 240]


def spritePositionedCorrectly(spritePos, currCycle):
    currCycleHoriz = (currCycle - 1) % 40
    return abs(currCycleHoriz - spritePos) <= 1


def drawPixel(x, currCycle):
    endChar = "\n" if cycleNewLine(currCycle) else ""
    if spritePositionedCorrectly(x, currCycle):
        print("#", end=endChar)
    else:
        print(".", end=endChar)


def main():
    lines = loadInput()
    currCycle = 1
    x = 1
    for i, line in enumerate(lines):
        lineInfo = line.split(" ")
        op = lineInfo[0]

        if op == "noop":
            drawPixel(x, currCycle)
            currCycle += 1
        else:
            drawPixel(x, currCycle)
            currCycle += 1
            drawPixel(x, currCycle)
            currCycle += 1
            x += int(lineInfo[1])


main()
