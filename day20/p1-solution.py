def loadInput():
    file = open('day20/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def moveVal(currList, i, num):
    for j, pair in enumerate(currList):
        if pair[0] == i and pair[1] == num:
            currList.pop(j)

            newInd = j + num
            if newInd == 0:
                currList.append(pair)
            else:
                newInd = newInd % len(currList)
                currList.insert(newInd, pair)

            return

    print("ERROR: not found")


def solution(initialList):
    currList = []
    for i, num in enumerate(initialList):
        currList.append((i, num))

    for i, num in enumerate(initialList):
        moveVal(currList, i, num)

    zeroInd = -1
    for j, pair in enumerate(currList):
        if pair[1] == 0:
            zeroInd = j
            break

    firstGroveInd = (zeroInd + 1000) % len(currList)
    firstGroveNum = currList[firstGroveInd][1]

    secondGroveInd = (zeroInd + 2000) % len(currList)
    secondGroveNum = currList[secondGroveInd][1]

    thirdGroveInd = (zeroInd + 3000) % len(currList)
    thirdGroveNum = currList[thirdGroveInd][1]

    return firstGroveNum + secondGroveNum + thirdGroveNum


def main():
    lines = loadInput()
    initialList = []
    for i, line in enumerate(lines):
        num = int(line)
        initialList.append(num)

    groveSum = solution(initialList)
    print(groveSum)


main()
