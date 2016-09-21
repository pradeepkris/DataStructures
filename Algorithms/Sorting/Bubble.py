a = [122,500,4,7,8,99,23,54, 1, 3]

print 'UNSORTED = ' + str( a )
# print 'N = ' + str( len(a) )
N = len(a)

for i in range(N-1,0,-1):
    for j in range(0, i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]


print 'SORTED   = ' + str( a )
