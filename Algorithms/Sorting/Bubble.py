a = [122,500,4,7,8,99,23,54, 1, 3]

print 'UNSORTED = ' + str( a )
N, arranged = len(a), 0

for i in range(N-1,0,-1):
    if arranged ==1:break
    for j in range(0, i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
        else:
            arranged = 1
            break

print 'SORTED   = ' + str( a )
