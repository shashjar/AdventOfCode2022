def loadInput():
    file = open('day3/input.txt', 'r')
    lines = file.readlines()
    return lines


def getGroupPriority(rucksack1, rucksack2, rucksack3):
    firstSet = set()
    for i in range(0, len(rucksack1)):
        firstSet.add(rucksack1[i])

    firstSecondSharedSet = set()
    for j in range(0, len(rucksack2)):
        if rucksack2[j] in firstSet:
            firstSecondSharedSet.add(rucksack2[j])

    for k in range(0, len(rucksack3)):
        if rucksack3[k] in firstSecondSharedSet:
            item = rucksack3[k]
            if ord(item) < ord('a'):
                return ord(item) - ord('A') + 27
            else:
                return ord(item) - ord('a') + 1


def main():
    lines = loadInput()
    groupPrioritySum = 0

    for i in range(0, len(lines), 3):
        groupPrioritySum += getGroupPriority(lines[i], lines[i+1], lines[i+2])

    print(groupPrioritySum)


main()
