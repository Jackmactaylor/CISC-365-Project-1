def bin_search(A,first,last,target):
    # returns index of target in A, if present
    # returns -1 if target is not present in A
    if first > last:
        return -1
    else:
        mid = (first+last)/2
    if A[mid] == target:
        return mid
    elif A[mid] > target:
        return bin_search(A,first,mid-1,target)
    else:
        return bin_search(A,mid+1,last,target)
