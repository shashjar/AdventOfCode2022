def loadInput():
    file = open('day8/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def visible(grid, r, c):
    height = grid[r][c]

    if r == 0 or r == len(grid) - 1 or c == 0 or c == len(grid[0]) - 1:
        return True

    above = True
    below = True
    left = True
    right = True

    for rAbove in range(0, r):
        if grid[rAbove][c] >= height:
            above = False

    for rBelow in range(r + 1, len(grid)):
        if grid[rBelow][c] >= height:
            below = False

    for cLeft in range(0, c):
        if grid[r][cLeft] >= height:
            left = False

    for cRight in range(c + 1, len(grid[0])):
        if grid[r][cRight] >= height:
            right = False

    return above or below or left or right


def solution(grid):
    numVisible = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if visible(grid, r, c):
                numVisible += 1

    print(numVisible)


def main():
    lines = loadInput()
    grid = [[] for i in range(len(lines))]
    for i, line in enumerate(lines):
        for num in line:
            grid[i].append(num)

    solution(grid)


main()
