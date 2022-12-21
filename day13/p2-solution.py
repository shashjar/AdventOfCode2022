def rec_lt(a, b):
    if type(a) == int and type(b) == list:
        return rec_lt([a], b)
    if type(a) == list and type(b) == int:
        return rec_lt(a, [b])
    if type(a) == list and type(b) == list:
        for l, r in zip(a, b):
            x = rec_lt(l, r)
            if x is not None:
                return x
        return rec_lt(len(a), len(b))
    if a == b:
        return None
    return a < b


class Signal:
    def __init__(self, arr):
        self.arr = arr

    def __lt__(self, other):
        return rec_lt(self.arr, other.arr)


with open('day13/input.txt', 'r') as f:
    array = [[Signal(eval(b)) for b in a.split('\n')]
             for a in f.read().split('\n\n')]

count = sum([(a < b) * (i + 1) for i, [a, b] in enumerate(array)])
print("Part 1:", count)

a, b = Signal([[2]]), Signal([[6]])
new_array = [a, b] + [signal for pair in array for signal in pair]
new_array.sort()
print("Part 2:", (new_array.index(a) + 1) * (new_array.index(b) + 1))
