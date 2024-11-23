# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
#
# Example,
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
#
# Reference,
# https://leetcode.com/problems/contiguous-array/


def max_len_cont_arr(arr):
    if len(arr) <= 1 or arr is None:
        return 0

    max_len = 0
    sum = 0
    tracking = {sum: -1}

    for i in range(len(arr)):
        if arr[i]:
            sum += 1
        else:
            sum -= 1

        if sum in tracking:
            curr_len = i - tracking[sum]
            max_len = max(max_len, curr_len)
        else:
            tracking[sum] = i

    return max_len


print (max_len_cont_arr([0,0,1]))
