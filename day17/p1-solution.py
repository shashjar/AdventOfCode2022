numRocks = 2022


def loadInput():
    file = open('day17/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def dropRock(rockInd, jetPattern, currGasJetInd, chamber):
    modRockInd = rockInd % 5
    rock = set()
    if modRockInd == 0:  # minus shape

    elif modRockInd == 1:  # plus shape

    elif modRockInd == 2:  # backwards L shape

    elif modRockInd == 3:  # vertical line shape

    else:  # square shape


def main():
    lines = loadInput()
    jetPattern = lines[0]
    currGasJetInd = 0
    chamber = [[]]

    for rockInd in range(numRocks):
        currGassJetInd = dropRock(rockInd, jetPattern, currGasJetInd, chamber)

    rockTowerHeight = getRockTowerHeight(chamber)
    print(rockTowerHeight)


main()
