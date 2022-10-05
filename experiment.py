"""
Group Project 1 Team 11
Name: Ryn Ou - 20183436, Decheng Zhu - STUDENT NUMBER, Jack Taylor - 20100745, Ruoshi Xia - 20167297

“I confirm that this submission is our own work and is consistent with the Queen's regulations on Academic Integrity.”

This file contains the sorting algorithm, generated array and 
measurement to experiment #1 and experiment #2
"""

import time
import random
import matplotlib.pyplot as plt
import numpy as np


def binary_search(A, first, last, target):
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
            return binary_search(A, first, mid - 1, target)
        else:
            return binary_search(A, mid + 1, last, target)


def trinary_search(A, first, last, target):
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
            return trinary_search(A, first, one_third - 1, target)
        elif A[two_third] == target:
            return two_third
        elif A[two_third] > target:
            return trinary_search(A, one_third + 1, two_third - 1, target)
        else:
            return trinary_search(A, two_third + 1, last, target)


def quick_sort(array):
    """
    This method sort the array using the quick sort algorithm
    Parameters:
        array - array to be sorted
        Returns - array in alphabetical order
    """
    L, E, G = [], [], []
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


def generate_sorted_array(n):
    """
    This method generate the random number and sort the array, only even number is included
    Parameters:
        n - the number of term to be generated
        Returns - arary in alphabetical ascending order
    """
    random_number = []
    number_of_terms = 0
    while number_of_terms != n:
        value = random.randint(0, 1e10)
        if value % 2 == 0:
            random_number.append(value)
            number_of_terms += 1
    return quick_sort(random_number)


def generate_search(array):
    """
    Use the generated array, product 10 times the same value and shuffle them
    This array will act as an term to be searched array
    Parameters:
    array - the generated alphabetical array
    Returns - a random search term list based on array
    """
    search_array = []
    for i in range(len(array)):
        for j in range(10):
            search_array.append(array[i])
    random.shuffle(search_array)
    return search_array


def generate_search_not_in_array(array):
    """
    Use the generated array, product 10 times the same value and shuffle them
    This array will act as an term to be searched array.
    This returns an array of search term that are not in array
    Parameters:
    array - the generated alphabetical array
    Returns - a random search term list based on array
    """
    search_array = []
    for i in range(len(array)):
        for j in range(10):
            # make the seach value odd number
            search_array.append(array[i] + 1)
    random.shuffle(search_array)
    return search_array


def measure_e1():
    """
    This method measure the total time of searching elements in the search array
    to the generated of n term array.
    It does two measurements, one using binary search, the other using trinary search
    Parameters:
        return timesTrinary - array with time measurement with trinary search
        return timesBinary - array with time measurement with binary search
    """

    N = [1000, 2000, 4000, 8000, 16000]
    binary_search_time = []
    trinary_search_time = []

    # loop through each array size
    for n in N:

        array = generate_sorted_array(n)
        search_term = generate_search(array)

        # measure trinary search
        start = time.process_time()
        for i in range(len(search_term)):
            assert trinary_search(array, 0, len(array) - 1, search_term[i]) != -1
        end = time.process_time()
        trinary_search_time.append(end - start)

        # measure binary search
        start = time.process_time()
        for i in range(len(search_term)):
            assert binary_search(array, 0, len(array) - 1, search_term[i]) != -1
        end = time.process_time()
        binary_search_time.append(end - start)

    return binary_search_time, trinary_search_time


def measure_e2():
    """
    This method measure the total time of searching elements that is not in the array
    This search represent the worst case scenario.
    It does two measurements, one using binary search, the other using trinary search
    Parameters:
        return an array with time measurement with trinary search
        return an array with time measurement with binary search
    """

    N = [1000, 2000, 4000, 8000, 16000]
    binary_search_time = []
    trinary_search_time = []

    # loop through each array size
    for n in N:
        array = generate_sorted_array(n)
        search_term = generate_search_not_in_array(array)

        # measure binary search
        start = time.process_time()
        for i in range(len(search_term)):
            result = binary_search(array, 0, len(array) - 1, search_term[i]) != -1
        end = time.process_time()
        binary_search_time.append(end - start)

        # measure trinary search
        start = time.process_time()
        for i in range(len(search_term)):
            result = trinary_search(array, 0, len(array) - 1, search_term[i]) != -1
        end = time.process_time()
        trinary_search_time.append(end - start)

    return binary_search_time, trinary_search_time


if __name__ == "__main__":
    N = [1000, 2000, 4000, 8000, 16000]

    # Experiment 1
    binary_search_time_1, trinary_search_time_1 = measure_e1()
    print("Experiment 1")
    print("N =", N)
    print("Binary Search Time:", binary_search_time_1)
    print("Trinary Search Time:", trinary_search_time_1)

    # Experiment 2
    binary_search_time_2, trinary_search_time_2 = measure_e2()
    print("Experiment 2")
    print("N =", N)
    print("Binary Search Time:", binary_search_time_2)
    print("Trinary Search Time:", trinary_search_time_2)

    x = np.array(N)
    y1 = np.array(binary_search_time_1)
    y2 = np.array(trinary_search_time_1)

    plt.plot(x, y1, 'o:r', x, y2, 'o:b')
    plt.xlabel("Sample (n)")
    plt.ylabel("Time taken")
    plt.title("Time vs n")
    plt.show()

    y3 = np.array(binary_search_time_2)
    y4 = np.array(trinary_search_time_2)

    plt.plot(x, y3, 'o:r', x, y4, 'o:b')
    plt.xlabel("Sample (n)")
    plt.ylabel("Time taken")
    plt.title("Time vs n")
    plt.show()

    ''' “I confirm that this submission is our own work and is consistent with the Queen's regulations on Academic 
    Integrity.” '''
