def loadInput():
    file = open('day21/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def getMonkeyNum(monkey, monkeys):
    monkeyOp = monkeys[monkey]
    if type(monkeyOp) == int:
        return monkeyOp

    if "+" in monkeyOp:
        monkeyOpInfo = monkeyOp.split(" + ")
        monkey1 = getMonkeyNum(monkeyOpInfo[0], monkeys)
        monkey2 = getMonkeyNum(monkeyOpInfo[1], monkeys)
        return monkey1 + monkey2
    elif "-" in monkeyOp:
        monkeyOpInfo = monkeyOp.split(" - ")
        monkey1 = getMonkeyNum(monkeyOpInfo[0], monkeys)
        monkey2 = getMonkeyNum(monkeyOpInfo[1], monkeys)
        return monkey1 - monkey2
    elif "*" in monkeyOp:
        monkeyOpInfo = monkeyOp.split(" * ")
        monkey1 = getMonkeyNum(monkeyOpInfo[0], monkeys)
        monkey2 = getMonkeyNum(monkeyOpInfo[1], monkeys)
        return monkey1 * monkey2
    elif "/" in monkeyOp:
        monkeyOpInfo = monkeyOp.split(" / ")
        monkey1 = getMonkeyNum(monkeyOpInfo[0], monkeys)
        monkey2 = getMonkeyNum(monkeyOpInfo[1], monkeys)
        return monkey1 / monkey2
    else:
        print("Invalid Operation")


def main():
    lines = loadInput()
    monkeys = {}
    for i, line in enumerate(lines):
        lineInfo = line.split(": ")
        monkey = lineInfo[0]
        op = lineInfo[1]

        if "+" not in op and "-" not in op and "*" not in op and "/" not in op:
            op = int(op)

        monkeys[monkey] = op

    rootNum = int(getMonkeyNum("root", monkeys))
    print(rootNum)


main()
