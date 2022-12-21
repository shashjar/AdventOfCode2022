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


def containsHuman(monkey, monkeys):
    if monkey == "humn":
        return True

    monkeyOp = monkeys[monkey]
    if type(monkeyOp) == int:
        return False

    return containsHuman(monkeyOp[0:4], monkeys) or containsHuman(monkeyOp[7:], monkeys)


def recurseDownHuman(monkey, monkeyVal, monkeys):
    monkeyOp = monkeys[monkey]

    subMonkey1 = monkeyOp[0:4]
    subMonkey2 = monkeyOp[7:]

    if subMonkey1 == "humn":
        subMonkey2Val = getMonkeyNum(subMonkey2, monkeys)

        if "+" in monkeyOp:
            return monkeyVal - subMonkey2Val
        elif "-" in monkeyOp:
            return monkeyVal + subMonkey2Val
        elif "*" in monkeyOp:
            return monkeyVal / subMonkey2Val
        elif "/" in monkeyOp:
            return monkeyVal * subMonkey2Val
        else:
            print("Invalid Operation")

    elif subMonkey2 == "humn":
        subMonkey1Val = getMonkeyNum(subMonkey1, monkeys)

        if "+" in monkeyOp:
            return monkeyVal - subMonkey1Val
        elif "-" in monkeyOp:
            return subMonkey1Val - monkeyVal
        elif "*" in monkeyOp:
            return monkeyVal / subMonkey1Val
        elif "/" in monkeyOp:
            return subMonkey1Val / monkeyVal
        else:
            print("Invalid Operation")

    elif containsHuman(subMonkey1, monkeys):
        subMonkey2Val = getMonkeyNum(subMonkey2, monkeys)

        if "+" in monkeyOp:
            return recurseDownHuman(subMonkey1, monkeyVal - subMonkey2Val, monkeys)
        elif "-" in monkeyOp:
            return recurseDownHuman(subMonkey1, monkeyVal + subMonkey2Val, monkeys)
        elif "*" in monkeyOp:
            return recurseDownHuman(subMonkey1, monkeyVal / subMonkey2Val, monkeys)
        elif "/" in monkeyOp:
            return recurseDownHuman(subMonkey1, monkeyVal * subMonkey2Val, monkeys)
        else:
            print("Invalid Operation")

    elif containsHuman(subMonkey2, monkeys):
        subMonkey1Val = getMonkeyNum(subMonkey1, monkeys)

        if "+" in monkeyOp:
            return recurseDownHuman(subMonkey2, monkeyVal - subMonkey1Val, monkeys)
        elif "-" in monkeyOp:
            return recurseDownHuman(subMonkey2, subMonkey1Val - monkeyVal, monkeys)
        elif "*" in monkeyOp:
            return recurseDownHuman(subMonkey2, monkeyVal / subMonkey1Val, monkeys)
        elif "/" in monkeyOp:
            return recurseDownHuman(subMonkey2, subMonkey1Val / monkeyVal, monkeys)
        else:
            print("Invalid Operation")

    print("Not found")


def getHumanNum(monkey1Val, monkey2Val, monkeys, monkey1ContainsHuman):
    rootOp = monkeys["root"]
    monkey1 = rootOp[0:4]
    monkey2 = rootOp[7:]

    if monkey1ContainsHuman:
        humanVal = recurseDownHuman(monkey1, monkey2Val, monkeys)
    else:
        humanVal = recurseDownHuman(monkey2, monkey1Val, monkeys)

    return humanVal


def solution(monkeys):
    rootOp = monkeys["root"]
    monkey1 = rootOp[0:4]
    monkey2 = rootOp[7:]
    monkey1Val = getMonkeyNum(monkey1, monkeys)
    monkey2Val = getMonkeyNum(monkey2, monkeys)

    if containsHuman(monkey1, monkeys):
        return getHumanNum(monkey1Val, monkey2Val, monkeys, True)
    else:
        return getHumanNum(monkey1Val, monkey2Val, monkeys, False)


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

    rootNum = int(solution(monkeys))
    print(rootNum)


main()
