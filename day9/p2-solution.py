def loadInput():
    file = open('day9/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def mustMoveTail(tailPos, headPos):
    if tailPos[0] == headPos[0]:
        newTailY = (tailPos[1] + headPos[1]) // 2
        return (tailPos[0], newTailY)
    elif tailPos[1] == headPos[1]:
        newTailX = (tailPos[0] + headPos[0]) // 2
        return (newTailX, tailPos[1])
    else:
        if (headPos[0] > tailPos[0] and headPos[1] > tailPos[1]):
            return (tailPos[0] + 1, tailPos[1] + 1)
        elif (headPos[0] > tailPos[0] and headPos[1] < tailPos[1]):
            return (tailPos[0] + 1, tailPos[1] - 1)
        elif (headPos[0] < tailPos[0] and headPos[1] > tailPos[1]):
            return (tailPos[0] - 1, tailPos[1] + 1)
        else:
            return (tailPos[0] - 1, tailPos[1] - 1)


def moveTail(tailPos, headPos):
    if abs(tailPos[0] - headPos[0]) <= 1 and abs(tailPos[1] - headPos[1]) <= 1:
        return tailPos
    else:
        return mustMoveTail(tailPos, headPos)


def getNewHeadPos(moveDirection, pos):
    if moveDirection == "U":
        return (pos[0], pos[1] + 1)
    elif moveDirection == "R":
        return (pos[0] + 1, pos[1])
    elif moveDirection == "D":
        return (pos[0], pos[1] - 1)
    elif moveDirection == "L":
        return (pos[0] - 1, pos[1])
    else:
        print("Invalid move direction")


def makeMove(moveDirection, numSteps, positions, positionsVisited):
    for _move in range(numSteps):
        for tail in range(1, 10):
            if tail == 1:
                newHeadPos = getNewHeadPos(moveDirection, positions[0])
                positions[0] = newHeadPos
                positions[tail] = moveTail(positions[tail], newHeadPos)
            else:
                positions[tail] = moveTail(
                    positions[tail], positions[tail - 1])
            positionsVisited.add(positions[9])


def main():
    lines = loadInput()

    positionsVisited = set()
    positionsVisited.add((0, 0))

    positions = {}
    for knot in range(10):
        positions[knot] = (0, 0)

    for i, line in enumerate(lines):
        moveInfo = line.split(" ")
        moveDirection = moveInfo[0]
        numSteps = int(moveInfo[1])
        makeMove(moveDirection, numSteps, positions, positionsVisited)

    print(len(positionsVisited))


main()
