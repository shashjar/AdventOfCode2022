def loadInput():
    file = open('day7/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def getFullPath(subDir, currDir):
    if currDir == "/":
        return currDir + subDir
    else:
        return currDir + "/" + subDir


def getTotalDirSize(dir, sizes, subDirs):
    totalDirSize = 0

    if dir in sizes:
        totalDirSize += sizes[dir]

    if dir in subDirs:
        for subDir in subDirs[dir]:
            totalDirSize += getTotalDirSize(subDir, sizes, subDirs)

    return totalDirSize


def getTotalSizeSum(sizes, subDirs, allDirs):
    totalSizeSum = 0

    for dir in allDirs:
        totalDirSize = getTotalDirSize(dir, sizes, subDirs)

        if totalDirSize <= 100000:
            totalSizeSum += totalDirSize

    print(totalSizeSum)


def main():
    lines = loadInput()
    currDir = ""
    sizes = {}
    prevDirs = {}
    subDirs = {}
    allDirs = set()

    i = 0
    while i < len(lines):
        line = lines[i]

        if line[0:4] == "$ ls":
            j = i + 1
            while j < len(lines) and lines[j][0] != "$":
                if lines[j][0:3] == "dir":
                    if currDir not in subDirs:
                        subDirs[currDir] = set()
                    subDirs[currDir].add(getFullPath(lines[j][4:], currDir))
                    dirPath = getFullPath(lines[j][4:], currDir)
                    prevDirs[dirPath] = currDir
                    allDirs.add(getFullPath(lines[j][4:], currDir))
                else:
                    lsOutput = lines[j].split(" ")
                    sizes[currDir] = int(lsOutput[0]) + sizes.get(currDir, 0)

                j += 1
            i = j

        elif line[0:6] == "$ cd /":
            currDir = "/"
            i += 1

        elif line[0:7] == "$ cd ..":
            currDir = prevDirs[currDir]
            i += 1

        elif line[0:4] == "$ cd":
            newDir = line[5:]
            dirPath = getFullPath(newDir, currDir)
            allDirs.add(dirPath)
            prevDirs[dirPath] = currDir
            currDir = getFullPath(newDir, currDir)
            i += 1

    getTotalSizeSum(sizes, subDirs, allDirs)


main()
