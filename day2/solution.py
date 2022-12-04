def loadInput():
    file = open('day2/input.txt', 'r')
    lines = file.readlines()
    return lines


def getScore(opponent, result):
    score = 0

    if result == "X":
        myPlay = "A" if opponent == "B" else "B" if opponent == "C" else "C"
        score += ord(myPlay) - ord("A") + 1
    elif result == "Y":
        score += 3 + ord(opponent) - ord("A") + 1
    else:
        myPlay = "A" if opponent == "C" else "B" if opponent == "A" else "C"
        score += 6 + ord(myPlay) - ord("A") + 1

    return score


def main():
    lines = loadInput()
    totalScore = 0

    for line in lines:
        opponent = line[0]
        result = line[2]

        totalScore += getScore(opponent, result)

    print(totalScore)


main()
