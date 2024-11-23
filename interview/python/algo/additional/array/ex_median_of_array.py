# Find the median of two sorted arrays.
# Example,
# arr1 = [1, 3, 5]
# arr2 = [2, 4, 6]
# median(arr1, arr2) = 3.5
#
# Reference:
# https://www.youtube.com/watch?v=LPFhl65R7ww
# https://www.byte-by-byte.com/median/

def median_of_arr(a1, a2):
    if len(a1) > len(a2):
        return median_of_arr(a2, a1)

    len_a1 = len(a1)
    len_a2 = len(a2)
    merged_len = len_a1 + len_a2

    low = 0
    high = len(a1)

    while low <= high:
        mid = (low + high )//2

        partition_a1 = mid
        # we need partion_a1 + partition_a2 = (merged_len + 1)//2
        partition_a2 = (merged_len + 1)//2 - partition_a1

        a1_max_left_part = float('-inf') if partition_a1 == 0 else a1[partition_a1-1]
        a1_min_right_part = float('inf') if partition_a1 == len_a1 else a1[partition_a1]

        a2_max_left_part = float('-inf') if partition_a2 == 0 else a2[partition_a2-1]
        a2_min_right_part = float('inf') if partition_a2 == len_a2 else a2[partition_a2]

        if a1_max_left_part <= a2_min_right_part and a2_max_left_part <= a1_min_right_part:
            if merged_len%2 == 0:
                return (max(a1_max_left_part, a2_max_left_part) + min(a1_min_right_part, a2_min_right_part))/float(2)
            else:
                return max(a1_max_left_part, a2_max_left_part)

        elif a1_max_left_part > a2_min_right_part:
            # we are too far on the right side
            high = partition_a1 - 1
        else:
            low = partition_a1 + 1

    # we only reach here if arrays are not sorted
    print ("array is not sorted or one of the given arrays is empty")
    return


a1 = [1, 3, 5, 8]
a2 = [2, 4, 6, 7]
print (median_of_arr(a1, a2))


a1 = [1, 3, 5, 8, 9]
a2 = []
print (median_of_arr(a1, a2))

a1 = []
a2 = [1, 3, 4, 8, 9]
print (median_of_arr(a1, a2))

a1 = [1,3]
a2 = [2]
print (median_of_arr(a1, a2))
