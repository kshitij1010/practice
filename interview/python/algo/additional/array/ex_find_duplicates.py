# Find duplicates in given array
#
# Find duplicates in O(n) time and O(1) extra space
# Given an array of n elements which contains elements from 0 to n-1, with any of these numbers appearing any number of times.
# Find these repeating numbers in O(n) and using only constant memory space.
#
# Reference:
# https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/


def find_duplicates(arr):
    if arr is None or len(arr) == 0:
        return []

    res = set()

    for i in range(len(arr)):
        if arr[abs(arr[i])] > 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        elif arr[abs(arr[i])] == 0:
            arr[abs(arr[i])] = -1
        else:
            res.add(abs(arr[i]))

    return res


print (find_duplicates([1, 6, 3, 1, 3, 6, 6,6,6,0,0]))
