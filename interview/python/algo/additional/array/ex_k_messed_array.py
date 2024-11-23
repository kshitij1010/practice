# K-Messed Array Sort
#
# Given an array of integers arr where each element is at most k places away from its sorted position,
# code an efficient function sortKMessedArray that sorts arr.
# For instance, for an input array of size 10 and k = 2,
# an element belonging to index 6 in the sorted array will be located at either index 4, 5, 6, 7 or 8 in the input array.
#
# Analyze the time and space complexities of your solution.
#
# Example:
#
# input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2
#
# output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# Reference:
# https://www.pramp.com/challenge/XdMZJgZoAnFXqwjJwnBZ

from heapq import heapify, heappop, heappush

def sort_k_messed_array(arr, k):
    if len(arr) <= 1:
        return arr

    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[::-1]
        return arr

    minh = arr[:k+1]
    heapify(minh)

    res = []

    for i in range(k+1, len(arr)):
        res.append(heappop(minh))
        heappush(minh, arr[i])

    while len(minh) > 0:
        res.append(heappop(minh))

    return res


a = [1]
print ("Input arr:", a)
print (sort_k_messed_array(a, 0))

a = [1, 0]
print ("\nInput arr:", a)
print (sort_k_messed_array(a, 1))

a = [1, 0, 3, 2]
print ("\nInput arr:", a)
print (sort_k_messed_array(a, 1))

a = [1, 0, 3, 2, 4, 5, 7, 6, 8]
print ("\nInput arr:", a)
print (sort_k_messed_array(a, 1))

a = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
print ("\nInput arr:", a)
print (sort_k_messed_array(a, 2))

a = [6, 1, 4, 11, 2, 0, 3, 7, 10, 5, 8, 9]
print ("\nInput arr:", a)
print (sort_k_messed_array(a, 6))

a = [34, 0, 100, 22]
print ("\nInput arr:", a)
print (sort_k_messed_array(a, 2))
