

####################################
#       Tuples
####################################
print 'Tuple Elements'
print '------------'
tup1 = ('physics', 'chemistry', 1997, 2000)
print tup1
print '\n'

# Navigating
print 'Navigating'
print '------------'
print 'tup[0]           : ' + str(tup1[0])
print '\n'


#Tuple Slicing
print 'Slicing'
print '------------'
print 'tup[:]           : ' + str(tup1[:])
print 'tup[0:len(tup1)] : ' + str(tup1[0:len(tup1)])
print 'tup[:2]          : ' + str(tup1[:2])
print 'tup[-2:]         : ' + str(tup1[-2:])
print 'tup[-3:-1]       : ' + str(tup1[-3:-1])
print 'tup[2:4]         : ' + str(tup1[2:4])
print '\n'

#Operations on Tuple

print 'Tuple Operations'
print '------------'

#Insert
print 'Insertint elements in Tuple is not allowed - IMMUTABLE'
#Delete
print 'Deleting  elements in Tuple is not allowed - IMMUTABLE'
#Update 
print 'Updating  elements in Tuple is not allowed - IMMUTABLE'
#Delete
print 'Deleting  elements in Tuple is not allowed - IMMUTABLE'

del tup1
try:
    tup1
    print 'tuple available'
except:
    print '\"del tup\" --> deletes the entire tuple ..'
print '\n'

tup1 = (1,2)
tup2 = (3,4)
print 'tup1             :' + str(tup1)
print 'tup2             :' + str(tup2) + '\n'

print 'Concantenation';
print '------------';
print 'tup1 + tup2      :' + str(tup1 + tup2) + '\n';
print 'Repetition';
print '------------';
print 'tup1 * 4         :' + str(tup1 * 4) + '\n';


print 'Tuple Built in Functions';
print '-------------------------'

print 'len(tup1)        :' + str(len(tup1))
print 'max(tup1)        :' + str(max(tup1))
print 'min(tup1)        :' + str(min(tup1))

alist = [1,2,3,4,5];
print 'alist            :' + str(alist);
print 'tuple(alist)     :' + str(tuple(alist))





























