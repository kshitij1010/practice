# Find the number which is not repeated in Array of integers, others are present for two times.
#
# Example,
# Input : 23, 34,56,21,21,56,78,23, 34
# Output: 23


def unique_elem(arr):
    if len(arr) == 0 or arr is None:
        return

    char_count = {}

    for i in range(len(arr)):
        if arr[i] in char_count:
            char_count[arr[i]] += 1
        else:
            char_count[arr[i]] = 1

    for key, val in char_count.items():
        if val == 1:
            return key

    return -1


# using XOR method
def unique_elem1(arr):
    res = arr[0]

    for i in range(1, len(arr)):
        res = res ^ arr[i]

    return res

a = [23, 34, 56, 21, 21, 56, 78, 23, 34]
print (unique_elem1(a))
