def loadInput():
    file = open('day14/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def getRockLocations(lines):
    rockLocations = set()

    for line in lines:
        lineInfo = line.split(" -> ")
        for j in range(len(lineInfo) - 1):
            fromInfo = lineInfo[j].split(",")
            fromInfo[0] = int(fromInfo[0])
            fromInfo[1] = int(fromInfo[1])
            toInfo = lineInfo[j + 1].split(",")
            toInfo[0] = int(toInfo[0])
            toInfo[1] = int(toInfo[1])

            # x values are equal (vertical line)
            if fromInfo[0] == toInfo[0]:
                if fromInfo[1] >= toInfo[1]:
                    for k in range(toInfo[1], fromInfo[1] + 1):
                        rockLocations.add((fromInfo[0], k))
                else:
                    for k in range(fromInfo[1], toInfo[1] + 1):
                        rockLocations.add((fromInfo[0], k))
            # y values are equal (horizontal line)
            else:
                if fromInfo[0] >= toInfo[0]:
                    for k in range(toInfo[0], fromInfo[0] + 1):
                        rockLocations.add((k, fromInfo[1]))
                else:
                    for k in range(fromInfo[0], toInfo[0] + 1):
                        rockLocations.add((k, fromInfo[1]))

    return rockLocations


def getLowestRockYCoord(rockLocations):
    maxYCoord = float('-inf')
    for loc in rockLocations:
        if loc[1] > maxYCoord:
            maxYCoord = loc[1]

    return maxYCoord


def main():
    lines = loadInput()

    # set of tuples with coordinates for all rocks
    rockLocations = getRockLocations(lines)

    # y coordinate of lowest rock (aka greatest y coordinate)
    lowestRockYCoord = getLowestRockYCoord(rockLocations)

    numSandUnitsDropped = 0  # number of sand units dropped so far
    # locations of all sand units dropped so far (that have come to rest)
    sandLocations = set()

    fallingIntoAbyss = False
    while not fallingIntoAbyss:  # loop until sand starts falling in the abyss
        sandLocation = (500, 0)
        while True:  # loop to drop this current sand unit until it comes to rest or falls forever
            belowLocation = (sandLocation[0], sandLocation[1] + 1)
            if belowLocation in rockLocations or belowLocation in sandLocations:  # below location blocked
                diagonalLeft = (sandLocation[0] - 1, sandLocation[1] + 1)
                if diagonalLeft in rockLocations or diagonalLeft in sandLocations:  # diagonal left location blocked
                    diagonalRight = (sandLocation[0] + 1, sandLocation[1] + 1)
                    if diagonalRight in rockLocations or diagonalRight in sandLocations:  # diagonal right location blocked
                        numSandUnitsDropped += 1
                        sandLocations.add(sandLocation)
                        break
                    else:  # diagonal right location not blocked
                        sandLocation = diagonalRight
                else:  # diagonal left location not blocked
                    sandLocation = diagonalLeft
            else:  # below location not blocked
                if sandLocation[1] > lowestRockYCoord:
                    fallingIntoAbyss = True
                    break
                sandLocation = belowLocation

    print(numSandUnitsDropped)


main()
