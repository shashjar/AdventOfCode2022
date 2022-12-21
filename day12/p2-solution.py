from collections import deque


def loadInput():
    file = open('day12/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def inBounds(location, grid):
    return location[0] >= 0 and location[0] < len(grid[0]) and location[1] >= 0 and location[1] < len(grid)


def validMove(fromLoc, toLoc, grid):
    fromChar = grid[fromLoc[1]][fromLoc[0]]
    toChar = grid[toLoc[1]][toLoc[0]]

    if fromChar == "S":
        fromChar = "a"
    elif fromChar == "E":
        fromChar = "z"

    if toChar == "S":
        toChar = "a"
    elif toChar == "E":
        toChar = "z"

    return ord(toChar) - ord(fromChar) <= 1


def solution(grid, startCoords, endCoords):
    queue = deque()
    nodeInfo = (startCoords[0], startCoords[1], 0)
    queue.append(nodeInfo)
    visited = set()
    visited.add((startCoords[0], startCoords[1]))

    while queue:
        currLocation = queue.popleft()
        if currLocation[0] == endCoords[0] and currLocation[1] == endCoords[1]:
            return currLocation[2]

        leftLocation = (currLocation[0] - 1,
                        currLocation[1], currLocation[2] + 1)
        rightLocation = (currLocation[0] + 1,
                         currLocation[1], currLocation[2] + 1)
        aboveLocation = (
            currLocation[0], currLocation[1] - 1, currLocation[2] + 1)
        belowLocation = (currLocation[0],
                         currLocation[1] + 1, currLocation[2] + 1)

        for nextLocation in [leftLocation, rightLocation, aboveLocation, belowLocation]:
            if inBounds(nextLocation, grid) and (nextLocation[0], nextLocation[1]) not in visited and validMove(currLocation, nextLocation, grid):
                visited.add((nextLocation[0], nextLocation[1]))
                queue.append(nextLocation)

    return float('inf')


def main():
    lines = loadInput()
    grid = []
    endCoords = (0, 0)
    for i, line in enumerate(lines):
        row = []
        for j, char in enumerate(line):
            row.append(char)
            if char == "E":
                endCoords = (j, i)
        grid.append(row)

    minNumSteps = float('inf')
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "a" or grid[y][x] == "S":
                numSteps = solution(grid, (x, y), endCoords)
                minNumSteps = min(minNumSteps, numSteps)

    print(minNumSteps)


main()
