rowNum = 2000000


def loadInput():
    file = open('day15/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def processLine(line, sensorBeacons):
    lineInfo = line.split(",")
    extraInfo = lineInfo[1].split(": closest beacon is at x=")

    sensorX = int(lineInfo[0][12:])
    sensorY = int(extraInfo[0][3:])
    beaconX = int(extraInfo[1])
    beaconY = int(lineInfo[2][3:])

    sensorBeacons[(sensorX, sensorY)] = (beaconX, beaconY)


def getManhattanDistance(loc1, loc2):
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])


def getNumberLocationsInRow(sensorY, manhattanDistance):
    deviation = abs(rowNum - sensorY)
    middleRowLength = manhattanDistance * 2 + 1
    return middleRowLength - (deviation * 2)


def solution(sensorBeacons):
    impossibleBeaconLocations = set()
    for sensor in sensorBeacons:
        beacon = sensorBeacons[sensor]
        manhattanDistance = getManhattanDistance(sensor, beacon)
        if sensor[1] - manhattanDistance <= rowNum and rowNum <= sensor[1] + manhattanDistance:
            numLocationsInRow = getNumberLocationsInRow(
                sensor[1], manhattanDistance)
            numLocationsOnEitherSide = (numLocationsInRow - 1) // 2
            for x in range(sensor[0] - numLocationsOnEitherSide, sensor[0] + numLocationsOnEitherSide + 1):
                if (x != beacon[0] or rowNum != beacon[1]) and getManhattanDistance(sensor, (x, rowNum)) <= manhattanDistance:
                    impossibleBeaconLocations.add((x, rowNum))

    return len(impossibleBeaconLocations)


def main():
    lines = loadInput()
    sensorBeacons = {}
    for i, line in enumerate(lines):
        processLine(line, sensorBeacons)

    numPositions = solution(sensorBeacons)
    print(numPositions)


main()
