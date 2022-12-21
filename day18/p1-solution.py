def loadInput():
    file = open('day18/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def getCubeSurfaceArea(cube, i, cubes):
    cubeSurfaceArea = 6
    for j in range(len(cubes)):
        if j != i:
            otherCube = cubes[j]
            if abs(cube[0] - otherCube[0]) == 1 and cube[1] == otherCube[1] and cube[2] == otherCube[2]:
                cubeSurfaceArea -= 1
            elif cube[0] == otherCube[0] and abs(cube[1] - otherCube[1]) == 1 and cube[2] == otherCube[2]:
                cubeSurfaceArea -= 1
            elif cube[0] == otherCube[0] and cube[1] == otherCube[1] and abs(cube[2] - otherCube[2]) == 1:
                cubeSurfaceArea -= 1

    return cubeSurfaceArea


def solution(cubes):
    surfaceArea = 0
    for i, cube in enumerate(cubes):
        surfaceArea += getCubeSurfaceArea(cube, i, cubes)

    return surfaceArea


def main():
    lines = loadInput()
    cubes = []
    for i, line in enumerate(lines):
        lineInfo = line.split(",")
        cubes.append([int(coord) for coord in lineInfo])

    surfaceArea = solution(cubes)
    print(surfaceArea)


main()
