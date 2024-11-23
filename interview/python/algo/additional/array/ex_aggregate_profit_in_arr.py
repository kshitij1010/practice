# You are given an array. Find the maximum profit you can get by summing the element of array.
# Only constrain is that you cannot include two neighbor elements in the sum.
#
# Example,
# Input: [2, 8, 3, 50, 7, 1]
# Output: 59        <= (8 + 50 + 1)
#
# Input: [50, 1, 3]
# Output: 53        <= (50 + 3)
#
# Input: [-50, 1, 3]
# Output: 3         <= (3)


def maximum_profit(arr):
    if arr is None or len(arr) == 0:
        return 0

    pick = arr[0]
    dont_pick = 0

    for i in range(1, len(arr)):
        # simple way
        # temp = pick
        # pick = dont_pick + arr[i]
        # dont_pick = max(temp, dont_pick)

        # pythonic way
        pick, dont_pick = dont_pick + arr[i], max(pick, dont_pick)

    return max(pick, dont_pick)



arr1 = [2, 8, 3, 50, 7, 1]
print (maximum_profit(arr1))

arr2 = [50, 1, 3]
print (maximum_profit(arr2))

arr3 = [-50, 1, 3]
print (maximum_profit(arr3))
