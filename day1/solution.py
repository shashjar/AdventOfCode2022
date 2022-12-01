def loadInput():
    file = open('day1/input.txt', 'r')
    lines = file.readlines()
    return lines


def main():
    lines = loadInput()

    firstElfCalories = 0
    secondElfCalories = 0
    thirdElfCalories = 0
    currElfCalories = 0

    for line in lines:
        if line == "\n":
            if currElfCalories >= firstElfCalories:
                thirdElfCalories = secondElfCalories
                secondElfCalories = firstElfCalories
                firstElfCalories = currElfCalories
            elif currElfCalories >= secondElfCalories:
                thirdElfCalories = secondElfCalories
                secondElfCalories = currElfCalories
            elif currElfCalories > thirdElfCalories:
                thirdElfCalories = currElfCalories
            currElfCalories = 0
        else:
            currElfCalories += int(line)

    totalCalories = firstElfCalories + secondElfCalories + thirdElfCalories
    print(totalCalories)


main()
