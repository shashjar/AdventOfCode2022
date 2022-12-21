# def loadInput():
#     file = open('day13/input.txt', 'r')
#     lines = file.read().splitlines()
#     return lines


# def rightOrder(left, right):
#     if type(left) == int and type(right) == list:
#         return rightOrder([left], right)
#     if type(left) == list and type(right) == int:
#         return rightOrder(left, [right])
#     if type(left) == list and type(right) == list:
#         for l, r in zip(left, right):
#             res = rightOrder(l, r)
#             if res is not None:
#                 return res
#         return rightOrder(len(left), len(right))
#     if left == right:
#         return None
#     return left < right


# def main():
#     lines = loadInput()
#     indexSum = 0
#     currIndex = 1
#     for i in range(0, len(lines), 3):
#         if rightOrder(lines[i], lines[i + 1]):
#             indexSum += currIndex
#         currIndex += 1

#     print(indexSum)


# main()

# # with open('day13input.txt', 'r') as f:
# #     array = [[Signal(eval(b)) for b in a.split('\n')]
# # #              for a in f.read().split('\n\n')]
# # count = sum([(a < b) * (i + 1) for i, [a, b] in enumerate(array)])
# # print("Part 1:", count)

# # a, b = Signal([[2]]), Signal([[6]])
# # new_array = [a, b] + [signal for pair in array for signal in pair]
# # new_array.sort()
# # print("Part 2:", (new_array.index(a) + 1) * (new_array.index(b) + 1))
