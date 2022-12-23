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


def wrapAround(currPos, currDir, grid):
    directions = ["R", "D", "L", "U"]
    counterDirMoves = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    dirInd = directions.index(currDir)
    dirMove = counterDirMoves[dirInd]

    r, c = currPos[0], currPos[1]

    while True:
        nextR, nextC = r + dirMove[0], c + dirMove[1]
        if nextR >= 0 and nextR < len(grid) and nextC >= 0 and nextC < len(grid[0]):
            if grid[nextR][nextC] == "e":
                if grid[r][c] == "#":
                    return None
                else:
                    return (r, c)
            else:
                r, c = nextR, nextC
        else:
            if grid[r][c] == "#":
                return None
            else:
                return (r, c)


def calculateNextTile(currPos, currDir, grid):
    directions = ["R", "D", "L", "U"]
    dirMoves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dirInd = directions.index(currDir)
    dirMove = dirMoves[dirInd]

    nextTile = (currPos[0] + dirMove[0], currPos[1] + dirMove[1])

    if nextTile[0] >= 0 and nextTile[0] < len(grid) and nextTile[1] >= 0 and nextTile[1] < len(grid[0]):
        if grid[nextTile[0]][nextTile[1]] == ".":  # open tile to move onto
            return nextTile

        # have to wrap around to the other side of the grid
        elif grid[nextTile[0]][nextTile[1]] == "e":
            return wrapAround(currPos, currDir, grid)

        # blocked by a solid wall, None indicates that no move is possible
        elif grid[nextTile[0]][nextTile[1]] == "#":
            return None
    else:  # have to wrap around to the other side of the grid
        return wrapAround(currPos, currDir, grid)


def moveNumTiles(currPos, currDir, grid, numTiles):
    for _ in range(numTiles):
        nextTile = calculateNextTile(currPos, currDir, grid)

        if nextTile == None:
            return currPos

        currPos = nextTile

    return currPos


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
            currPos = moveNumTiles(currPos, currDir, grid, move)
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

    path = getPathList(lines[-1])

    password = solution(grid, path)
    print(password)


main()
