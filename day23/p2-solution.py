def loadInput():
    file = open('day23/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def noAdjacentElves(elf, elves, directions):
    for dir in directions:
        for loc in dir:
            neighborLoc = (elf[0] + loc[0], elf[1] + loc[1])
            if neighborLoc in elves:
                return False

    return True


def empty(elf, elves, dir):
    for loc in dir:
        neighborLoc = (elf[0] + loc[0], elf[1] + loc[1])
        if neighborLoc in elves:
            return False

    return True


def updateProposedDestinations(elves, proposedMoves):
    for elf in elves:
        dest = proposedMoves[elf]
        for otherElf in elves:
            if otherElf != elf:
                otherDest = proposedMoves[otherElf]
                if otherDest == dest:
                    proposedMoves[elf] = elf
                    proposedMoves[otherElf] = otherElf


def simulateRound(elves, directions):
    proposedMoves = {}
    for elf in elves:
        proposedMoves[elf] = elf

        if noAdjacentElves(elf, elves, directions):
            continue

        for dir in directions:
            if empty(elf, elves, dir):
                proposedMoves[elf] = (elf[0] + dir[0][0], elf[1] + dir[0][1])
                break

    updateProposedDestinations(elves, proposedMoves)

    newElves = set()
    for elf in elves:
        dest = proposedMoves[elf]
        newElves.add(dest)

    if newElves == elves:
        return None

    directions.append(directions.pop(0))
    return newElves


def solution(elves):  # set of coordinates (r, c) where elves are located (origin top left of initial grid)
    directions = [
        [(-1, 0), (-1, 1), (-1, -1)],
        [(1, 0), (1, 1), (1, -1)],
        [(0, -1), (-1, -1), (1, -1)],
        [(0, 1), (-1, 1), (1, 1)]
    ]  # [N, NE, NW], [S, SE, SW], [W, NW, SW], [E, NE, SE]

    roundNum = 1
    while True:
        elves = simulateRound(elves, directions)
        if elves == None:
            return roundNum
        roundNum += 1


def main():
    lines = loadInput()
    grove = [[] for _ in range(len(lines))]
    elves = set()
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            grove[r].append(char)
            if char == "#":
                elves.add((r, c))

    numRounds = solution(elves)
    print(numRounds)


main()
