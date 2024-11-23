# Merge Sorted Arrays
#
# In order to win the prize for most cookies sold,
# my friend Alice and I are going to merge our Girl Scout Cookies orders and enter as one unit.
#
# Each order is represented by an "order id" (an integer).
# We have our lists of orders sorted numerically already, in lists.
# Write a function to merge our lists of orders into one sorted list.
#
# Example:
#
# my_list     = [3, 4, 6, 10, 11, 15]
# alices_list = [1, 5, 8, 12, 14, 19]
#
# Output: [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]


def merge_lists(arr1, arr2):
    if arr1 is None or len(arr1) == 0:
        return arr2

    if arr2 is None or len(arr2) == 0:
        return arr1

    res = []

    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <  arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    while i < len(arr1):
        res.append(arr1[i])
        i += 1

    while j < len(arr2):
        res.append(arr2[j])
        j += 1

    return res

arr1 = [3, 4, 6, 10, 11, 15]
arr2 = [1, 5, 8, 12, 14, 19]
print (merge_lists(arr1, arr2))
