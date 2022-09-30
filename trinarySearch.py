def trin_search(A,first,last,target):
    # returns index of target in A, if present
    # returns -1 if target is not present in A
    if first > last:
        return -1
    else:
        one_third = first + (last-first)/3
        two_thirds = first + 2*(last-first)/3
    if A[one_third] == target:
        return one_third
    elif A[one_third] > target:
        # search the left-hand third
        return trin_search(A,first,one_third-1,target)
    elif A[two_thirds] == target:
        return two_thirds
    elif A[two_thirds] > target:
        # search the middle third
        return trin_search(A,one_third+1,two_thirds-1,target)
    else:
        # search the right-hand third
        return trin_search(A,two_thirds+1,last,target)
