
def InsertionSort(Arr):

    for i in range(1,len(Arr)):
        print '---------------------------------------------------'
        if Arr[i-1] > Arr[i]:
            Arr[i-1], Arr[i] = Arr[i], Arr[i-1]

        print 'check I --->',i,'&', i-1, Arr

        for j in range(i-1, 0, -1):

            if Arr[j-1] > Arr[j]:
                Arr[j-1], Arr[j] = Arr[j], Arr[j-1]
            print 'check j ***>',j,'&', j-1, Arr

        if i > 20: break

Arr = [9,7,8,5,6,6,1,-1]
InsertionSort(Arr)
