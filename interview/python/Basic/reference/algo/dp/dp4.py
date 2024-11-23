# Find the Longest increasing subsequence with the highest sum
# Example,
# Input: [4, 6, 1, 3, 8, 4, 6]
# Output: [4, 6, 8] (sums to  18 which is the highest sum)
# https://www.youtube.com/watch?v=99ssGWhLPUE


def find_longest_increasing_subseq_with_highest_sum(arr):
    LIS = arr[:]
    LIS_index = list(range(len(arr)))

    for end in range(1, len(arr)):
        for j in range(end):
            if arr[end] > arr[j]:
                if LIS[end] < LIS[j]+arr[end]:
                    LIS[end] = LIS[j]+arr[end]
                    LIS_index[end] = j

    sum = max(LIS)
    print("Max sum is :", sum)
    i = LIS.index(sum)
    res = []
    while i > 0 and i < len(arr):
        print(arr[i])
        i = LIS_index[i]
        if i == LIS_index[i]:
            print(arr[i])
            break

    return


find_longest_increasing_subseq_with_highest_sum([4, 6, 1, 3, 8, 4, 6])
