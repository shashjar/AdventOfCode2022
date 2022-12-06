def loadInput():
    file = open('day6/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def unique(chars):
    charSet = set()
    for c in chars:
        if c in charSet:
            return False
        charSet.add(c)

    return True


def main():
    lines = loadInput()
    for line in lines:
        currChars = ""
        for i, char in enumerate(line):
            if len(currChars) == 4 and unique(currChars):
                print(i)
                return
            elif len(currChars) == 4:
                currChars = currChars[1:] + char
            else:
                currChars += char


main()
