def loadInput():
    file = open('day10/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def updateRes(res, x, currCycle):
    if currCycle in [20, 60, 100, 140, 180, 220]:
        res += x * currCycle

    return res


def main():
    lines = loadInput()
    currCycle = 1
    x = 1
    res = 0
    for i, line in enumerate(lines):
        lineInfo = line.split(" ")
        op = lineInfo[0]

        if op == "noop":
            currCycle += 1
            res = updateRes(res, x, currCycle)
        else:
            currCycle += 1
            res = updateRes(res, x, currCycle)
            currCycle += 1
            x += int(lineInfo[1])
            res = updateRes(res, x, currCycle)

    print(res)


main()
