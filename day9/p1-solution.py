def loadInput():
    file = open('day9/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def mustMoveTail(tailPos, headPos, positionsVisited):
    if tailPos[0] == headPos[0]:
        newTailY = (tailPos[1] + headPos[1]) // 2
        tailPos[1] = newTailY
    elif tailPos[1] == headPos[1]:
        newTailX = (tailPos[0] + headPos[0]) // 2
        tailPos[0] = newTailX
    else:
        if (headPos[0] > tailPos[0] and headPos[1] > tailPos[1]):
            tailPos[0] = tailPos[0] + 1
            tailPos[1] = tailPos[1] + 1
        elif (headPos[0] > tailPos[0] and headPos[1] < tailPos[1]):
            tailPos[0] = tailPos[0] + 1
            tailPos[1] = tailPos[1] - 1
        elif (headPos[0] < tailPos[0] and headPos[1] > tailPos[1]):
            tailPos[0] = tailPos[0] - 1
            tailPos[1] = tailPos[1] + 1
        else:
            tailPos[0] = tailPos[0] - 1
            tailPos[1] = tailPos[1] - 1

    positionsVisited.add((tailPos[0], tailPos[1]))


def moveTail(tailPos, headPos, positionsVisited):
    positionsVisited.add((tailPos[0], tailPos[1]))

    if abs(tailPos[0] - headPos[0]) <= 1 and abs(tailPos[1] - headPos[1]) <= 1:
        return
    else:
        mustMoveTail(tailPos, headPos, positionsVisited)


def processMove(moveDirection, numSteps, tailPos, headPos, positionsVisited):
    positionsVisited.add((tailPos[0], tailPos[1]))

    for _move in range(numSteps):
        if moveDirection == "U":
            headPos[1] = headPos[1] + 1
            moveTail(tailPos, headPos, positionsVisited)
        elif moveDirection == "R":
            headPos[0] = headPos[0] + 1
            moveTail(tailPos, headPos, positionsVisited)
        elif moveDirection == "D":
            headPos[1] = headPos[1] - 1
            moveTail(tailPos, headPos, positionsVisited)
        elif moveDirection == "L":
            headPos[0] = headPos[0] - 1
            moveTail(tailPos, headPos, positionsVisited)
        else:
            print("Invalid move direction")


def main():
    lines = loadInput()

    positionsVisited = set()
    positionsVisited.add((0, 0))
    tailPos = {0: 0, 1: 0}
    headPos = {0: 0, 1: 0}
    for i, line in enumerate(lines):
        moveInfo = line.split(" ")
        moveDirection = moveInfo[0]
        numSteps = int(moveInfo[1])
        processMove(moveDirection, numSteps, tailPos,
                    headPos, positionsVisited)

    print(len(positionsVisited))


main()
