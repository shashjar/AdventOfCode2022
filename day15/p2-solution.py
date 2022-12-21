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


def getNumberLocationsInRow(sensorY, locationY, manhattanDistance):
    deviation = abs(locationY - sensorY)
    middleRowLength = manhattanDistance * 2 + 1
    return middleRowLength - (deviation * 2)


def solution(sensorBeacons):
    impossibleBeaconLocations = set()
    for sensor in sensorBeacons:
        print(sensor)
        beacon = sensorBeacons[sensor]
        manhattanDistance = getManhattanDistance(sensor, beacon)
        for y in range(sensor[1] - manhattanDistance, sensor[1] + manhattanDistance + 1):
            numLocationsInRow = getNumberLocationsInRow(
                sensor[1], y, manhattanDistance)
            numLocationsOnEitherSide = (numLocationsInRow - 1) // 2
            for x in range(sensor[0] - numLocationsOnEitherSide, sensor[0] + numLocationsOnEitherSide + 1):
                if (x != beacon[0] or y != beacon[1]) and getManhattanDistance(sensor, (x, y)) <= manhattanDistance:
                    impossibleBeaconLocations.add((x, y))

    beacons = set()
    for sensor in sensorBeacons:
        beacons.add(sensorBeacons[sensor])

    for x in range(0, 4000001):
        for y in range(0, 4000001):
            if (x, y) not in impossibleBeaconLocations and (x, y) not in sensorBeacons and (x, y) not in beacons:
                print(x, y, 4000000 * x + y)


def main():
    lines = loadInput()
    sensorBeacons = {}
    for i, line in enumerate(lines):
        processLine(line, sensorBeacons)

    tuningFrequency = solution(sensorBeacons)
    print(tuningFrequency)


main()
