import binarySearch
import trinarySearch
import random as r
import math

#range of values of n stored in array
n_range_arr = [1000, 2000, 4000, 8000, 16000]


def generate_n_random_int(n_range):
    n_random_arr = []
    for i in range(n_range):
        n_random_arr.append(r.randint(0, n_range))
    return n_random_arr

#recursive merge sort
def merge_sort(A, start, end):
    #While there is still unsorted
    if start < end:
        mid = math.floor((start + end) / 2)
        merge_sort(A, start, mid)
        merge_sort(A, mid + 1, end)
        merge(A, start, mid, end)

#does not work feel free to remove/edit
def merge(A, start, mid, end):

    print("A: " + str(A))
    print("start: " + str(start))
    print("mid: " + str(mid))
    print("end: " + str(end))
        
    left_end = mid - start + 1
    right_end = end - mid
    #Initialize an array of Nones to avoid index out of bound error
    left_arr = [None] * (left_end)
    right_arr = [None] * (right_end)
    
    print("left array size:" + str(len(left_arr)))
    print("right array size:" + str(len(right_arr)))
    print("left end value:" + str(left_end))
    print("right end value:" + str(right_end))
    
    for i in range(0, left_end):
        print("i: " + str(i))
        left_arr[i] = A[start + i - 1]
        
    for j in range(0, right_end):
        print("j: " + str(j))
        right_arr[j] = A[mid + j]
    
    print("left array: " + str(left_arr))
    print("right array: " + str(right_arr))
    print("\n")
    
    #eft_arr[left_end] = math.inf
    #right_arr[right_end] = math.inf
    left_arr.append(math.inf)
    right_arr.append(math.inf)
    i = 0
    j = 0
    
    for k in range(start, end):
        if left_arr[i] <= right_arr[j]:
            A[k] = left_arr[i]
            i += 1
        else:
            A[k] = right_arr[j]
            j += 1
            


#random_array = generate_n_random_int(n_range_arr[0])
random_array = generate_n_random_int(10)

    
print(random_array)

random_array = merge_sort(random_array, 0, len(random_array) - 1)

print(random_array)
