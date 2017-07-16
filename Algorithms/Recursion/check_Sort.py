a = [1, 5, 6, 7, 8, 10]


def isSorted(anArray):
    if len(anArray) == 1:
        return True
    else:
        return anArray[0] < anArray[1] and isSorted(anArray[1:])

print isSorted(a)
