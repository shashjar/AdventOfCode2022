cubeSideLen = 50


def loadInput():
    file = open('day22/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def getStartingPos(grid):
    row = 0
    col = -1
    for i, char in enumerate(grid[0]):
        if char == ".":
            col = i

    return (row, col)


def getPathList(pathString):
    pathList = []
    lastLetterInd = -1
    for i in range(len(pathString)):
        if pathString[i] in "LR":
            num = int(pathString[lastLetterInd + 1: i])
            pathList.append(num)
            pathList.append(pathString[i])
            lastLetterInd = i

    if lastLetterInd < len(pathString) - 1:
        num = int(pathString[lastLetterInd + 1:])
        pathList.append(num)

    return pathList


def getWrapRegions(currPos, currDir, cubeSideLen):
    r, c = currPos[0], currPos[1]
    if r < cubeSideLen:
        fromRegion = 1
    elif r < 2 * cubeSideLen:
        if c < cubeSideLen:
            fromRegion = 2
        elif c < 2 * cubeSideLen:
            fromRegion = 3
        else:
            fromRegion = 4
    else:
        if c < 3 * cubeSideLen:
            fromRegion = 5
        else:
            fromRegion = 6

    if fromRegion == 1:
        if currDir == "R":
            toRegion = 6
            newDir = "L"
        elif currDir == "L":
            toRegion = 3
            newDir = "D"
        elif currDir == "U":
            toRegion = 2
            newDir = "D"

    elif fromRegion == 2:
        if currDir == "D":
            toRegion = 5
            newDir = "U"
        elif currDir == "L":
            toRegion = 6
            newDir = "U"
        elif currDir == "U":
            toRegion = 1
            newDir = "D"

    elif fromRegion == 3:
        if currDir == "D":
            toRegion = 5
            newDir = "R"
        elif currDir == "U":
            toRegion = 1
            newDir = "R"

    elif fromRegion == 4:
        if currDir == "R":
            toRegion = 6
            newDir = "D"

    elif fromRegion == 5:
        if currDir == "D":
            toRegion = 2
            newDir = "U"
        elif currDir == "L":
            toRegion = 3
            newDir = "U"

    else:
        if currDir == "R":
            toRegion = 1
            newDir = "L"
        elif currDir == "D":
            toRegion = 2
            newDir = "R"
        elif currDir == "U":
            toRegion = 4
            newDir = "L"

    return fromRegion, toRegion, newDir


def wrapAround(currPos, currDir, grid):
    fromRegion, toRegion, newDir = getWrapRegions(
        currPos, currDir, cubeSideLen)

    r, c = currPos[0], currPos[1]

    if fromRegion == 1:
        if toRegion == 6:
            nextR = 3 * cubeSideLen - r - 1
            nextC = 4 * cubeSideLen - 1
        elif toRegion == 3:
            nextR = cubeSideLen
            nextC = cubeSideLen + r
        elif toRegion == 2:
            nextR = cubeSideLen
            nextC = cubeSideLen - (c % cubeSideLen) - 1

    elif fromRegion == 2:
        if toRegion == 5:
            nextR = 3 * cubeSideLen - 1
            nextC = 3 * cubeSideLen - c - 1
        elif toRegion == 6:
            nextR = 3 * cubeSideLen - 1
            nextC = 4 * cubeSideLen - (r % cubeSideLen) - 1
        elif toRegion == 1:
            nextR = 0
            nextC = 3 * cubeSideLen - (r % cubeSideLen) - 1

    elif fromRegion == 3:
        if toRegion == 5:
            nextR = 3 * cubeSideLen - (c % cubeSideLen) - 1
            nextC = 2 * cubeSideLen
        elif toRegion == 1:
            nextR = c % cubeSideLen
            nextC = 2 * cubeSideLen

    elif fromRegion == 4:  # toRegion must be 6
        nextR = 2 * cubeSideLen
        nextC = 4 * cubeSideLen - (r % cubeSideLen) - 1

    elif fromRegion == 5:
        if toRegion == 2:
            nextR = 2 * cubeSideLen - 1
            nextC = cubeSideLen - (c % cubeSideLen) - 1
        elif toRegion == 3:
            nextR = 2 * cubeSideLen - 1
            nextC = 2 * cubeSideLen - (r % cubeSideLen) - 1

    else:
        if toRegion == 1:
            nextR = cubeSideLen - (r % cubeSideLen) - 1
            nextC = 3 * cubeSideLen - 1
        elif toRegion == 2:
            nextR = 2 * cubeSideLen - (c % cubeSideLen) - 1
            nextC = 0
        elif toRegion == 4:
            nextR = 2 * cubeSideLen - (c % cubeSideLen) - 1
            nextC = 3 * cubeSideLen - 1

    nextR, nextC = int(nextR), int(nextC)
    if grid[nextR][nextC] == "#":
        return None, currDir
    else:
        return (nextR, nextC), newDir


def calculateNextTile(currPos, currDir, grid):
    directions = ["R", "D", "L", "U"]
    dirMoves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dirInd = directions.index(currDir)
    dirMove = dirMoves[dirInd]

    nextTile = (currPos[0] + dirMove[0], currPos[1] + dirMove[1])

    if nextTile[0] >= 0 and nextTile[0] < len(grid) and nextTile[1] >= 0 and nextTile[1] < len(grid[0]):
        if grid[nextTile[0]][nextTile[1]] == ".":  # open tile to move onto
            return nextTile, currDir

        # have to wrap around to the other side of the grid
        elif grid[nextTile[0]][nextTile[1]] == "e":
            return wrapAround(currPos, currDir, grid)

        # blocked by a solid wall, None indicates that no move is possible
        elif grid[nextTile[0]][nextTile[1]] == "#":
            return None, currDir
    else:  # have to wrap around to the other side of the grid
        return wrapAround(currPos, currDir, grid)


def moveNumTiles(currPos, currDir, grid, numTiles):
    for _ in range(numTiles):
        nextTile, nextDir = calculateNextTile(currPos, currDir, grid)

        if nextTile == None:
            return currPos, currDir

        currPos = nextTile
        currDir = nextDir

    return currPos, currDir


def turnDirection(currDir, turnDir):
    directions = ["R", "D", "L", "U"]
    dirInd = directions.index(currDir)
    if turnDir == "R":  # turn clockwise
        newInd = (dirInd + 1) % len(directions)
        newDir = directions[newInd]
    else:  # turn counterclockwise
        newDir = directions[dirInd - 1]

    return newDir


def solution(grid, path):  # grid is a 2D list, path is a list
    currPos = getStartingPos(grid)  # position is indicated as (row, col)
    currDir = "R"

    for i, move in enumerate(path):
        if i % 2 == 0:  # move some number of tiles in the current direction
            currPos, currDir = moveNumTiles(currPos, currDir, grid, move)
        else:  # turn clockwise or counterclockwise in place
            currDir = turnDirection(currDir, move)

    rowVal = 1000 * (currPos[0] + 1)
    colVal = 4 * (currPos[1] + 1)
    if currDir == "R":
        facingVal = 0
    elif currDir == "D":
        facingVal = 1
    elif currDir == "L":
        facingVal = 2
    else:
        facingVal = 3

    return rowVal + colVal + facingVal


def processGrid(grid):
    side1 = []
    side2 = []
    for r in range(cubeSideLen):
        side1.append(grid[r][cubeSideLen: 2 * cubeSideLen])
        side2.append(grid[r][2 * cubeSideLen:])

    side3 = []
    for r in range(cubeSideLen, 2 * cubeSideLen):
        side3.append(grid[r][cubeSideLen: 2 * cubeSideLen])

    side4 = []
    side5 = []
    for r in range(2 * cubeSideLen, 3 * cubeSideLen):
        side4.append(grid[r][0: cubeSideLen])
        side5.append(grid[r][cubeSideLen: 2 * cubeSideLen])

    side6 = []
    for r in range(3 * cubeSideLen, 4 * cubeSideLen):
        side6.append(grid[r][0:cubeSideLen])

    emptyRow = ["e"] * cubeSideLen

    newGrid = []

    for r in range(cubeSideLen):
        newGrid.append(emptyRow * 2 + side1[r] + emptyRow)

    for r in range(cubeSideLen):
        newGrid.append(side2[r] + side3[r] + side4[r] + emptyRow)

    for r in range(cubeSideLen):
        newGrid.append(emptyRow * 2 + side5[r] + side6[r])

    return newGrid


def main():
    lines = loadInput()
    grid = [[] for _ in range(len(lines) - 2)]
    for i, line in enumerate(lines):
        if line == "":
            break
        for char in line:
            if char == " ":
                char = "e"
            grid[i].append(char)

    maxRowLen = -1
    for row in grid:
        maxRowLen = max(maxRowLen, len(row))

    for row in grid:
        if len(row) < maxRowLen:
            row += ["e"] * (maxRowLen - len(row))

    grid = processGrid(grid)
    path = getPathList(lines[-1])

    password = solution(grid, path)
    print(password)


main()
