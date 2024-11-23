# Getting a Different Number (From pramp)
#
# Given an unsorted array arr of unique nonnegative integers,
# implement a function getDifferentNumber that finds the smallest nonnegative integer that is NOT in the array.
#
# Even if your programming language of choice doesn’t have that restriction (like Python),
# assume that the maximum value an integer can have is MAX_INT = 2^31-1. So, for instance,
# the operation MAX_INT + 1 would be undefined in our case.
#
# Your algorithm should be efficient, both from a time and a space complexity perspectives.
#
# Solve first for the case when you’re NOT allowed to modify the input arr.
# If successful and still have time,
# see if you can come up with an algorithm with an improved space complexity when modifying arr is allowed.
# Do so without trading off the time complexity.
#
# Analyze the time and space complexities of your algorithm.
#
# Eg-1,
# input:  arr = [1,3,0,2]
# output: 4
# Reference:
# https://www.pramp.com/challenge/aK6V5GVZ9MSPqvG1vwQp


# if we are not allowed to modify the array
def get_different_number_unmodified_input(arr):
    for i in range(len(arr)):

        if i not in input:
            return i

    return len(arr)

# if we are allowed to modify the array
def get_different_number(arr):
    arr_size = len(arr)

    i = 0

    while i < arr_size:
        temp = arr[i]
        while temp < arr_size and temp != i:
            arr[i], arr[temp] = arr[temp], arr[i]
            temp = arr[i]
        i += 1

    for j in range(arr_size):
        if j != arr[j]:
            return j

    return arr_size


def print_res(arr, expected):
    print ("\n\n\ninput arr:", arr)
    print ("Expected:", expected)
    print ("Actual Output: ")
    # print (get_different_number_unmodified_input(arr))
    print (get_different_number(arr))



# print ("Method 1: Method where modifying the arr is not allowed")
print ("Method 2: Method where modifying the arr is allowed")


print_res([0], 1)
print_res([0,1,2], 3)
print_res([1,3,0,2], 4)
print_res([100000], 0)
print_res([1,0,3,4,5], 2)
print_res([0,100000], 1)
print_res([0,99999,100000], 1)
print_res([0,5,4,1,3,6,2], 7)
