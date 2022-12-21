def loadInput():
    file = open('day16/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def processLine(line, adjList):
    valve = line[6:8]
    info = line.split(";")
    valveInfo = info[0].split("=")
    flowRate = int(valveInfo[1])
    if "valves" in info[1]:
        tunnelInfo = info[1].split("valves ")
    else:
        tunnelInfo = info[1].split("valve ")
    tunnelsList = tunnelInfo[1].split(", ")
    adjList[valve] = (flowRate, tunnelsList)


def solution(adjList, currValve, currTime, currPressureRelease, valvesReleased):
    if currTime >= 30:
        return currPressureRelease

    if currValve not in valvesReleased:  # current valve not already released
        flowRate = adjList[currValve][0]
        totalValvePressureRelease = flowRate * (30 - currTime)
        maxRemainingPressureRelease = 0
        newValvesReleased = set()
        for elt in valvesReleased:
            newValvesReleased.add(elt)
        newValvesReleased.add(currValve)
        for neighborValve in adjList[currValve][1]:
            neighborValvePressureRelease = solution(
                adjList, neighborValve, currTime + 2, totalValvePressureRelease + currPressureRelease, newValvesReleased)
            maxRemainingPressureRelease = max(
                maxRemainingPressureRelease, neighborValvePressureRelease)
        totalPressureReleaseWithValveRelease = totalValvePressureRelease + \
            maxRemainingPressureRelease  # max pressure release if we release this valve

        maxRemainingPressureRelease = 0
        for neighborValve in adjList[currValve][1]:
            neighborValvePressureRelease = solution(
                adjList, neighborValve, currTime + 1, currPressureRelease, valvesReleased)
            # max pressure release if we do not release this valve
            maxRemainingPressureRelease = max(
                maxRemainingPressureRelease, neighborValvePressureRelease)

        return max(totalPressureReleaseWithValveRelease, maxRemainingPressureRelease)

    else:  # current valve already released
        maxRemainingPressureRelease = 0
        for neighborValve in adjList[currValve][1]:
            neighborValvePressureRelease = solution(
                adjList, neighborValve, currTime + 1, currPressureRelease, valvesReleased)
            maxRemainingPressureRelease = max(
                maxRemainingPressureRelease, neighborValvePressureRelease)

        return maxRemainingPressureRelease


def main():
    lines = loadInput()
    adjList = {}
    for i, line in enumerate(lines):
        processLine(line, adjList)

    maxPressureRelease = solution(adjList, "AA", 0, 0, set())
    print(maxPressureRelease)


main()
