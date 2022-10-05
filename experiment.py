"""
Group Project 1 Team 11
Name: Ryn Ou, Decheng Zhu, Jack Taylor, Ruoshi Xia

This file contains the sorting algorithm, generated array and 
measurement to experiment #1 and experiment #2
"""

import time
import random

def bin_search(A,first,last,target):
    """
    This method search the target in the array A using the binary search method

    Parameters: 
        A - array to be searched
        first - index 0, the head index
        last - (maxindex - 1), the tail index
        target - this is the target to be searched in array A

        Returns - the int searched index
    """
    if first > last:
        return -1
    else:
        mid = (first + last) // 2
        if A[mid] == target:
            return mid
        elif A[mid] > target:
            return bin_search(A,first,mid - 1,target)
        else:
            return bin_search(A,mid + 1,last,target)

def trin_search(A,first,last,target):
    """
    This method search the target in the array A using the trinary search method, iterate for every 1/3 of the array

    Parameters: 
        A - array to be searched
        first - index 0, the head index
        last - (maxindex - 1), the tail index
        target - this is the target to be searched in array A

        Returns - the int searched index
    """
    if first > last:
        return -1
    else:
        a = (last - first) 
        one_third = first + a // 3
        two_third = first + 2 * a // 3
        if A[one_third] == target:
            return one_third
        elif A[one_third] > target:
            # search the left-hand third
            return trin_search(A,first,one_third - 1,target)
        elif A[two_third] == target:
            return two_third
        elif A[two_third] > target:
            return  trin_search(A,one_third + 1,two_third - 1,target)
        else:
            return trin_search(A,two_third + 1,last,target)

def quick_sort(array):
    """
    This method sort the array using the quick sort algorithm

    Parameters: 
        array - array to be sorted

        Returns - array in alphabetical order
    """
    L,E,G = [],[],[]
    if len(array) > 1:
        for x in array:
            if x > array[0]:
                G.append(x)
            elif x == array[0]:
                E.append(x)
            else:
                L.append(x)
        return quick_sort(L) + E + quick_sort(G)
    else:
        return array

def generate_sortedarray(n):
    """
    This method generate the random number and sort the array, only even number is included

    Parameters: 
        n - the number of term to be generated

        Returns - arary in alphabetical ascending order
    """
    randomNumber = []
    numberOfTerms = 0
    while numberOfTerms != n:
        value = random.randint(0,1e10)
        if ( value % 2 == 0 ):
            randomNumber.append(value)
            numberOfTerms += 1
    return quick_sort(randomNumber)

def generate_search( array ):
    """
    Use the generated array, product 10 times the same value and shuffle them
    This array will act as an term to be searched array

    Parameters: 
    array - the generated alphabetical array

    Returns - a random search term list based on array
    """
    searchArray = []
    for i in range(len(array)):
        for j in range(10):
            searchArray.append(array[i])
    random.shuffle(searchArray)
    return searchArray

def generate_search_not_in_array( array ):
    """
    Use the generated array, product 10 times the same value and shuffle them
    This array will act as an term to be searched array.

    This returns an array of search term that are not in array

    Parameters: 
    array - the generated alphabetical array

    Returns - a random search term list based on array
    """
    searchArray = []
    for i in range(len(array)):
        for j in range(10):
            # make the seach value odd number
            searchArray.append(array[i]+1)
    random.shuffle(searchArray)
    return searchArray

def measure():
    """
    This method measure the total time of searching elements in the search array
    to the generated of n term array.

    It does two measurements, one using binary search, the other using trinary search

    Parameters: 
        return timesTrinary - array with time measurement with trinary search
        return timesBinary - array with time measurement with binary search
    """

    N = [1000,2000,4000,8000,16000]
    timesTrinary = []
    timesBinary = []

    # loop through each array size
    for n in N:

        array = generate_sortedarray(n)
        searchTerm = generate_search(array)

        ## measure trinary search
        start = time.process_time()
        for i in range(len(searchTerm)):
            assert trin_search(array,0,len(array) - 1,searchTerm[i]) != -1
        end = time.process_time()
        timesTrinary.append(end - start)

        ## measure binary search 
        start = time.process_time()
        for i in range(len(searchTerm)):
            assert bin_search(array,0,len(array) - 1,searchTerm[i]) != -1
        end = time.process_time()
        timesBinary.append(end - start)

    return timesTrinary,timesBinary


def measure2():
    """
    This method measure the total time of searching elements that is not in the array
    This search represent the worst case scenario.

    It does two measurements, one using binary search, the other using trinary search

    Parameters: 
        return timesTrinary - array with time measurement with trinary search
        return timesBinary - array with time measurement with binary search
    """
    
    N = [1000,2000,4000,8000,16000]
    timesTrinary = []
    timesBinary = []

    # loop through each array size
    for n in N:

        array = generate_sortedarray(n)
        searchTerm = generate_search_not_in_array(array)

        ## measure trinary search
        start = time.process_time()
        for i in range(len(searchTerm)):
            result = trin_search(array,0,len(array) - 1,searchTerm[i]) != -1
        end = time.process_time()
        timesTrinary.append(end - start)

        ## measure binary search 
        start = time.process_time()
        for i in range(len(searchTerm)):
            result = bin_search(array,0,len(array) - 1,searchTerm[i]) != -1
        end = time.process_time()
        timesBinary.append(end - start)

    return timesTrinary,timesBinary


if __name__ == "__main__":

    N = [1000,2000,4000,8000,16000]

    ## experiment 1
    trin_time,bin_time = measure()
    print("experiment 1")
    print("N",N)
    print("trin_time",trin_time)
    print("bin_time",bin_time)

    ## experiment 2
    trin_time,bin_time = measure2()
    print("experiment 2")
    print("N",N)
    print("trin_time",trin_time)
    print("bin_time",bin_time)
