# Length of the largest subarray with contiguous elements
#
# Given an array of distinct integers,
# find length of the longest subarray which contains numbers that can be arranged in a continuous sequence.
#
# Example,
# Input:  arr[] = {10, 12, 11};
# Output: Length of the longest contiguous subarray is 3
#
# Input:  arr[] = {14, 12, 11, 20};
# Output: Length of the longest contiguous subarray is 2
#
# Input:  arr[] = {1, 56, 58, 57, 90, 92, 94, 93, 91, 45};
# Output: Length of the longest contiguous subarray is 5
#
# Reference:
# https://www.geeksforgeeks.org/length-largest-subarray-contiguous-elements-set-1/

def subarr_cont_elems(arr):
    if len(arr) == 0 or arr is None:
        return

    ans = 0
    for i in range(len(arr)-1):
        mn = arr[i]
        mx = arr[i]
        for j in range(i+1, len(arr)):
            mn = min(mn, arr[j])
            mx = max(mx, arr[j])

            if (mx-mn) == (j-i):
                ans = max(ans, j-i+1)

    return ans



print (subarr_cont_elems([1,5,6,7,10,50,51,52,53])) # 4
print (subarr_cont_elems([10,12,11])) # 3
print (subarr_cont_elems([14,12,11,20])) # 2
print (subarr_cont_elems([1,56,58,57,90,92,94,93,91,45])) # 5
