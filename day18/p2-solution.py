def loadInput():
    file = open('day18/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def airPocket(cubeAdj, cubes, minX, maxX, minY, maxY, minZ, maxZ):
    sidesBounded = 0
    x = cubeAdj[0]
    y = cubeAdj[1]
    z = cubeAdj[2]

    for boundMinX in range(x, minX - 1, -1):
        if [boundMinX, y, z] in cubes:
            sidesBounded += 1
            break
    for boundMaxX in range(x, maxX + 1):
        if [boundMaxX, y, z] in cubes:
            sidesBounded += 1
            break
    for boundMinY in range(y, minY - 1, -1):
        if [x, boundMinY, z] in cubes:
            sidesBounded += 1
            break
    for boundMaxY in range(y, maxY + 1):
        if [x, boundMaxY, z] in cubes:
            sidesBounded += 1
            break
    for boundMinZ in range(z, minZ - 1, -1):
        if [x, y, boundMinZ] in cubes:
            sidesBounded += 1
            break
    for boundMaxZ in range(z, maxZ + 1):
        if [x, y, boundMaxZ] in cubes:
            sidesBounded += 1
            break

    return sidesBounded == 6


def getCubeSurfaceArea(cube, cubes, minX, maxX, minY, maxY, minZ, maxZ):
    cubeSurfaceArea = 6
    if [cube[0] + 1, cube[1], cube[2]] in cubes:
        cubeSurfaceArea -= 1
    elif airPocket([cube[0] + 1, cube[1], cube[2]], cubes, minX, maxX, minY, maxY, minZ, maxZ):
        cubeSurfaceArea -= 1

    if [cube[0] - 1, cube[1], cube[2]] in cubes:
        cubeSurfaceArea -= 1
    elif airPocket([cube[0] - 1, cube[1], cube[2]], cubes, minX, maxX, minY, maxY, minZ, maxZ):
        cubeSurfaceArea -= 1

    if [cube[0], cube[1] + 1, cube[2]] in cubes:
        cubeSurfaceArea -= 1
    elif airPocket([cube[0], cube[1] + 1, cube[2]], cubes, minX, maxX, minY, maxY, minZ, maxZ):
        cubeSurfaceArea -= 1

    if [cube[0], cube[1] - 1, cube[2]] in cubes:
        cubeSurfaceArea -= 1
    elif airPocket([cube[0], cube[1] - 1, cube[2]], cubes, minX, maxX, minY, maxY, minZ, maxZ):
        cubeSurfaceArea -= 1

    if [cube[0], cube[1], cube[2] + 1] in cubes:
        cubeSurfaceArea -= 1
    elif airPocket([cube[0], cube[1], cube[2] + 1], cubes, minX, maxX, minY, maxY, minZ, maxZ):
        cubeSurfaceArea -= 1

    if [cube[0], cube[1], cube[2] - 1] in cubes:
        cubeSurfaceArea -= 1
    elif airPocket([cube[0], cube[1], cube[2] - 1], cubes, minX, maxX, minY, maxY, minZ, maxZ):
        cubeSurfaceArea -= 1

    return cubeSurfaceArea


def solution(cubes, minX, maxX, minY, maxY, minZ, maxZ):
    surfaceArea = 0
    for i, cube in enumerate(cubes):
        surfaceArea += getCubeSurfaceArea(cube,
                                          cubes, minX, maxX, minY, maxY, minZ, maxZ)

    return surfaceArea


def main():
    lines = loadInput()
    cubes = []
    minX = float('inf')
    maxX = float('-inf')
    minY = float('inf')
    maxY = float('-inf')
    minZ = float('inf')
    maxZ = float('-inf')

    for i, line in enumerate(lines):
        lineInfo = line.split(",")
        x = int(lineInfo[0])
        y = int(lineInfo[1])
        z = int(lineInfo[2])

        minX = min(minX, x)
        maxX = max(maxX, x)
        minY = min(minY, y)
        maxY = max(maxY, y)
        minZ = min(minZ, z)
        maxZ = max(maxZ, z)

        cubes.append([x, y, z])

    surfaceArea = solution(cubes, minX, maxX, minY, maxY, minZ, maxZ)
    print(surfaceArea)


main()
