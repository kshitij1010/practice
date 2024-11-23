# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
# Reference:
# https://leetcode.com/problems/rotate-array/
# https://www.youtube.com/watch?v=8kyZPizZzWc


# using extra space
def rotate_arr_basic(arr, k):
    # copying arr to clone,
    # if slice is not used then basically they are same and reference would be to sam memory
    # that is why instead of using "clone = arr" using following
    clone = arr[:]
    len_arr = len(arr)
    for i in range(len_arr):
        arr[(i+k)%len_arr] = clone[i]

    return

a = [1,2,3,4,5,6,7]
rotate_arr_basic(a, 3)
print (a) # should return [5,6,7,1,2,3,4]


# Optimized: without using extra space
def reverse_arr(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return

def rotate_arr(arr, k):
    len_arr = len(arr)
    k = k%len_arr
    reverse_arr(arr, 0, len_arr-1)
    reverse_arr(arr, 0, k-1)
    reverse_arr(arr, k, len_arr-1)
    return

a = [1,2,3,4,5,6,7]
rotate_arr(a, 3)
print (a) # should return [5,6,7,1,2,3,4]
