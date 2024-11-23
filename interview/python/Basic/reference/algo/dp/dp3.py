# LC300. Longest Increasing Subsequence
# Find the Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/
# Given an array of numbers, find the length of the longest increasing subsequence in the array.
# The subsequence does not necessarily have to be contiguous.
# For example,
# Input: [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
# Output: 6 (Explanation: the increasing arr is 0, 2, 6, 9, 11, 15)



def find_longest_increasing_subseq(arr):
    if len(arr) == 0 or arr is None:
        return

    LIS = [1]*(len(arr))
    L = list(range(len(arr)))

    for end in range(1, len(arr)):
        for j in range(end):
            if arr[end] > arr[j]:
                if LIS[end] < LIS[j]+1:
                    LIS[end] = LIS[j]+1
                    L[end] = j

    mx = max(LIS)
    print ("Len of longest increasing subseq is :", mx)

    # following part is for printing the subsequence arr
    i = LIS.index(mx)
    res = []
    while i > 0 and i < len(arr):
        print (arr[i], end =" ")
        i = L[i]
        if i == L[i]:
            print (arr[i])
            break
    print ()
    return


find_longest_increasing_subseq([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) # 6
find_longest_increasing_subseq([ 10, 22, 9, 33, 21, 50, 41, 60]) # 5
