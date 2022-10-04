import time
import random
random.seed(120)
def bin_search(A,first,last,target):
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
    array = [ random.randint(0,1e10) for i in range(n) ] 
    array = sorted(array)
    return array





def measure(f1,f2):
    def func():
        N = [1000,2000,4000,8000,16000]
        times1 = []
        times2 = []
        for n in N:
            array = generate_sortedarray(n)
            start = time.process_time()
            for i in range(n):
                for j in range(10):
                    assert f1(array,0,len(array) - 1,array[i]) != -1
            end   = time.process_time()
            times1.append(end - start)
            ## measure binary search 
            start = time.process_time()
            for i in range(n):
                for j in range(10):
                    assert f2(array,0,len(array) - 1,array[i]) != -1
            end   = time.process_time()
            times2.append(end - start)
        return times1,times2
    return func

N = [1000,2000,4000,8000,16000]
trin_time,bin_time= measure(trin_search,bin_search)()
print("experiment 1")
print("N",N)
print("trin_time",trin_time)
print("bin_time",bin_time)


def generate_search(n):
    l = [i for i in range(2 * n)]
    search_array,numbers = [i for i in l if i % 2 == 0],[i for i in l if i % 2 == 1]
    return search_array,numbers

def measure2(f1,f2):
    def func():
        N = [1000,2000,4000,8000,16000]
        times1 = []
        times2 = []
        for n in N:
            searched,array = generate_search(n)
            start = time.process_time()
            for i in range(n):
                for j in range(10):
                    assert f1(array,0,len(array) - 1,searched[i]) == -1
            end   = time.process_time()
            times1.append(end - start)
            ## measure binary search 
            start = time.process_time()
            for i in range(n):
                for j in range(10):
                    assert f2(array,0,len(array) - 1,searched[i]) == -1
            end   = time.process_time()
            times2.append(end - start)
        return times1,times2
    return func


N = [1000,2000,4000,8000,16000]
trin_time,bin_time= measure2(trin_search,bin_search)()
print("experiment 2")
print("N",N)
print("trin_time",trin_time)
print("bin_time",bin_time)