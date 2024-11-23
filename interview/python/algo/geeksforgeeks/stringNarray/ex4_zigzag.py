# Convert array into Zig-Zag fashion
#
# Given an array of DISTINCT elements,
# rearrange the elements of array in zig-zag fashion in O(n) time.
# The converted array should be in form a < b > c < d > e < f.
#
# Example:
# Input:  arr[] = {4, 3, 7, 8, 6, 2, 1}
# Output: arr[] = {3, 7, 4, 8, 2, 6, 1}
#
# Input:  arr[] =  {1, 4, 3, 2}
# Output: arr[] =  {1, 4, 2, 3}
#
# Reference:
# https://www.geeksforgeeks.org/convert-array-into-zig-zag-fashion/


def zigzag(arr):
    # we will use flag to know the current condition we need to check
    # if flag is 1 then we need to maintaine "<"
    # else we need to maintaine ">" (if flag is 0)

    # we will start with "<"
    flag = 1

    # since we will check the condition with next element,
    # we need to loop until the second last element
    for i in range(len(arr)-1):
        if flag:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        flag = 1 - flag # to invert the flag

    return arr


def print_res(input, expected):
    print ("Input:", input)
    print ("Expected:", expected)
    output = zigzag(input)
    print ("Actual:", output)
    if expected != output:
        print ("Wrong answer\n")
    else:
        print ("Correct answer\n")


print_res([4, 3, 7, 8, 6, 2, 1], [3, 7, 4, 8, 2, 6, 1])
print_res([1, 4, 3, 2], [1, 4, 2, 3])
