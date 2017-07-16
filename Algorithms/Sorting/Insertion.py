
def InsertionSort(Arr):
    for i in range(1, len(Arr)):
        if Arr[i] > Arr[i-1]:
            Arr[i], Arr[i-1] = Arr[i-1], Arr[i]

            for j in range(i-1, 0, -1):
                if Arr[j] > Arr[j-1]:
                    Arr[j], Arr[j-1] = Arr[j-1], Arr[j]

    return Arr

Arr = [7,9,8,5,6,6,-3,1]
print InsertionSort(Arr)
