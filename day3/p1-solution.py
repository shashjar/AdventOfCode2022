def loadInput():
    file = open('day3/input.txt', 'r')
    lines = file.readlines()
    return lines


def getPriority(rucksack):
    firstHalfSet = set()
    for i in range(0, len(rucksack) // 2):
        firstHalfSet.add(rucksack[i])

    for j in range(len(rucksack) // 2, len(rucksack)):
        if rucksack[j] in firstHalfSet:
            if ord(rucksack[j]) < ord('a'):
                return ord(rucksack[j]) - ord('A') + 27
            else:
                return ord(rucksack[j]) - ord('a') + 1


def main():
    lines = loadInput()
    prioritySum = 0

    for line in lines:
        prioritySum += getPriority(line)

    print(prioritySum)


main()
