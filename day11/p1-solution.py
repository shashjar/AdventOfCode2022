def loadInput():
    file = open('day11/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def processMonkey(monkeyInfo):
    startingItems = monkeyInfo[1][18:].split(",")
    for i in range(len(startingItems)):
        startingItems[i] = int(startingItems[i])
    operation = monkeyInfo[2][19:]
    test = int(monkeyInfo[3].split("  Test: divisible by ")[1])
    trueMonkeyInd = int(monkeyInfo[4][29])
    falseMonkeyInd = int(monkeyInfo[5][30])

    # list of information for this monkey - last element is number of inspections
    return [startingItems, operation, test, trueMonkeyInd, falseMonkeyInd, 0]


def applyInspectionOperation(initialWorryLevel, operation):
    if "+" in operation:
        operationInfo = operation.split(" + ")
        return initialWorryLevel + int(operationInfo[1])
    elif "old * old" in operation:
        return initialWorryLevel**2
    else:
        operationInfo = operation.split(" * ")
        return initialWorryLevel * int(operationInfo[1])


def runRound(monkeys):
    for monkeyInd in range(len(monkeys)):
        monkey = monkeys[monkeyInd]
        itemInd = 0
        while itemInd < len(monkey[0]):
            monkey[5] += 1  # increment number of items inspected

            currWorryLevel = applyInspectionOperation(
                monkey[0][itemInd], monkey[1])
            currWorryLevel //= 3
            if currWorryLevel % monkey[2] == 0:
                toMonkey = monkey[3]
                monkeys[toMonkey][0].append(currWorryLevel)
                monkey[0].pop(itemInd)
            else:
                toMonkey = monkey[4]
                monkeys[toMonkey][0].append(currWorryLevel)
                monkey[0].pop(itemInd)


def main():
    lines = loadInput()
    i = 0
    monkeys = {}
    while i < len(lines):
        monkey = processMonkey(lines[i:i+6])
        monkeys[i // 7] = monkey
        i += 7

    numRounds = 20
    for _ in range(numRounds):
        runRound(monkeys)

    sortedMonkeys = sorted(monkeys.values(), key=lambda m: -m[5])
    print(sortedMonkeys[0][5] * sortedMonkeys[1][5])


main()
