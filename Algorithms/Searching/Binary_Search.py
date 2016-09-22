###############################
##   RECURSION
###############################
def Binary_Search_I(Arr, X):

    l_bound, u_bound = 0, len(Arr)
    mid = u_bound/2

    if l_bound == u_bound: return "Search Element " + str(X) + " Not Found"

    if X == Arr[mid]: return "Search Element " + str(X) + " Found"
    else:
        if X > Arr[mid]: new_Arr = Arr[ mid + 1 : u_bound  ]
        else: new_Arr = Arr[l_bound : mid]
        return Binary_Search_I(new_Arr, X)

###############################
##   NO RECURSION
###############################
def Binary_Search_II(Arr, X):
    l_bound, u_bound = 0, len(Arr)

    while l_bound < u_bound :
        mid = ( u_bound + l_bound ) / 2

        if X == Arr[mid]: return "Search Element " + str(X) + " Found"
        else:
            if X < Arr[mid]: u_bound = mid - 1
            else: l_bound = mid + 1

    return "Search Element " + str(X) + " Not Found"

###############################
##   USAGE
###############################
Arr = [2,34,5,6,6,7,8,933,33,44,55,66]
print "Array = ", Arr
print '-----------'
print Binary_Search_I(Arr, 55)
print Binary_Search_I(Arr, 1)
print '-----------'
print Binary_Search_II(Arr, 66)
print Binary_Search_II(Arr, 3343)
print '-----------'
