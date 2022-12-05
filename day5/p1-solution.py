def loadInput():
    file = open('day5/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def capitalLetter(s):
    if len(s) != 1:
        return False

    return ord(s) - ord("A") >= 0 and ord("Z") - ord(s) >= 0


def processMoves(stacks, moves):
    for move in moves:
        moveInfo = move.split(" ")
        numToMove = int(moveInfo[1])
        fromStack = int(moveInfo[3])
        toStack = int(moveInfo[5])

        for i in range(numToMove):
            crate = stacks[fromStack - 1].pop(0)
            stacks[toStack - 1].insert(0, crate)


def main():
    lines = loadInput()
    numStacks = 9

    stacks = [[] for i in range(numStacks)]
    for line in lines:
        if line[1] == "1":
            break

        ind = 1
        while ind // 4 <= numStacks and ind < len(line):
            if capitalLetter(line[ind]):
                stackNum = ind // 4
                stacks[stackNum].append(line[ind])
            ind += 4

    processMoves(stacks, lines[10:])

    res = ""
    for stack in stacks:
        res += stack[0]

    print(res)


main()
