def loadInput():
    file = open('day8/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def viewingDistance(grid, r, c):
    height = grid[r][c]

    above = 0
    for rAbove in range(r - 1, -1, -1):
        above += 1
        if grid[rAbove][c] >= height:
            break

    below = 0
    for rBelow in range(r + 1, len(grid)):
        below += 1
        if grid[rBelow][c] >= height:
            break

    left = 0
    for cLeft in range(c - 1, -1, -1):
        left += 1
        if grid[r][cLeft] >= height:
            break

    right = 0
    for cRight in range(c + 1, len(grid[0])):
        right += 1
        if grid[r][cRight] >= height:
            break

    return above * below * left * right


def solution(grid):
    maxViewingDistance = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            maxViewingDistance = max(
                maxViewingDistance, viewingDistance(grid, r, c))

    print(maxViewingDistance)


def main():
    lines = loadInput()
    grid = [[] for i in range(len(lines))]
    for i, line in enumerate(lines):
        for num in line:
            grid[i].append(int(num))

    solution(grid)


main()
