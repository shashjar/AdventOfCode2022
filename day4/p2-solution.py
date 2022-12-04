def loadInput():
    file = open('day4/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def overlap(start1, start2, end1, end2):
    if start1 >= start2 and end2 >= start1:
        return True
    elif start2 >= start1 and end1 >= start2:
        return True

    return False


def main():
    lines = loadInput()
    count = 0
    for line in lines:
        pair = line.split(",")
        firstElf = pair[0].split("-")
        secondElf = pair[1].split("-")

        if overlap(int(firstElf[0]), int(secondElf[0]), int(firstElf[1]), int(secondElf[1])):
            count += 1

    print(count)


main()
