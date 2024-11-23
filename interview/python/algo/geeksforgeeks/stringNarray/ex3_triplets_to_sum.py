# Count triplets with sum smaller than a given value
#
# Given an array of distinct integers and a sum value.
# Find count of triplets with sum smaller than given sum value.
# Expected Time Complexity is O(n2).
#
# Reference:
# https://www.geeksforgeeks.org/count-triplets-with-sum-smaller-that-a-given-value/


def count_triplets(arr, s):
    arr.sort()

    arr_size = len(arr)
    count = 0

    for i in range(arr_size-2):
        # to demonstrate two pointer method, the same method as follow up can be used
        j = i + 1
        k = arr_size - 1
        while j < k:
            sum_of_three_elem = arr[i] + arr[j] + arr[k]
            if sum_of_three_elem < s:
                count += (k-j)
                j += 1
            else:
                k -= 1
    return count

arr1 = [2, 7, 4, 0, 9, 5, 1, 3]
s1 = 20
print (count_triplets(arr1, s1))

arr2 = [5, 1, 3, 4, 7]
s2 = 12
print (count_triplets(arr2, s2))








# Follow up question
# to find the Triplet [3 elements sums up to the given number]
def find_arr_triplet(arr, s):
    arr.sort()

    arr_size = len(arr)

    for i in range(arr_size):
        first = s - arr[i]
        # to demonstrate two pointer method, the same method as follow up can be used
        j = i + 1
        k = arr_size - 1
        while j < k:
            sum_of_two_elem = arr[j] + arr[k]
            if sum_of_two_elem == first:
                return [arr[i], arr[j], arr[k]]
            elif sum_of_two_elem > first:
                k -= 1
            else:
                j += 1
    return []

arr3 = [2, 7, 4, 0, 9, 5, 1, 3]
s3 = 20
print (find_arr_triplet(arr3, s3))

arr4 = [5, 1, 3, 4, 7]
s4 = 12
print (find_arr_triplet(arr4, s4))




# Follow up question
# to find the quadruplet [4 elements sums up to the given number]
def find_arr_quadruplet(arr, s):
    arr.sort()

    for k in range(len(arr)):
        first = s - arr[k]
        for j in range(k+1,len(arr)-1):
            d = {}
            second = first - arr[j]
            for i in range(j+1,len(arr)):
                if arr[i] in d:
                    return [arr[k], arr[j], d[arr[i]], arr[i]]
                else:
                    d.update({(second-arr[i]):arr[i]})

    return []


arr = [2, 7, 4, 0, 9, 5, 1, 3]
s = 20

print (find_arr_quadruplet(arr, s))
