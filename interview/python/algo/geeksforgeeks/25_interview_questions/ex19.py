# Given an array of integers, update the index with multiplication of previous and next integers
#
# Example,
# Input: 2 , 3, 4, 5, 6
# Output: 2*3, 2*4, 3*5, 4*6, 5*6
#
# https://www.geeksforgeeks.org/replace-every-array-element-by-multiplication-of-previous-and-next/


# using extra space
def product_of_pre_next(arr):
    if len(arr) == 0 or arr is None:
        return []

    if len(arr) == 1:
        return arr

    res = []

    for i in range(len(arr)):
        if i == 0:
            res.append(arr[i] * arr[i+1])
        elif i == len(arr)-1:
            res.append(arr[i] * arr[i-1])
        else:
            res.append(arr[i-1] * arr[i+1])
    return res

# without using extra space, by modifying the given array
def product_of_pre_next2(arr):
    if len(arr) == 0 or arr is None:
        return []

    if len(arr) == 1:
        return arr

    prev = arr[0]
    # first elems
    arr[0] = arr[0] * arr[1]
    for i in range(1, len(arr)-1):
        prev, arr[i] = arr[i], prev * arr[i+1]

    # last elems
    arr[-1] = prev * arr[-1]

    return


print (product_of_pre_next([]))
print (product_of_pre_next([7]))
print (product_of_pre_next([17,3]))
print (product_of_pre_next([1,2,3,4,5]))
print (product_of_pre_next([2,3,4,5,6]))


arr1 = []
arr2 = [7]
arr3 = [17,3]
arr4 = [1,2,3,4,5]
arr5 = [2,3,4,5,6]
product_of_pre_next2(arr1)
product_of_pre_next2(arr2)
product_of_pre_next2(arr3)
product_of_pre_next2(arr4)
product_of_pre_next2(arr5)
print (arr1, arr2, arr3, arr4, arr5)
