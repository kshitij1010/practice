# Maximum size rectangle binary sub-matrix with all 1s
# Given a binary matrix, find the maximum size rectangle binary-sub-matrix with all 1’s.
# Example:
#
# Input :   0 1 1 0
#           1 1 1 1
#           1 1 1 1
#           1 1 0 0
#
# Output :  8
#
# Reference:
# https://www.geeksforgeeks.org/maximum-size-rectangle-binary-sub-matrix-1s/


def histogram_area(arr):
    i = 0
    stack = []
    area = 0
    max_area = 0

    while i < len(arr):
        if not stack or arr[stack[-1]] <= arr[i]:
            stack.append(i)
            i += 1
        else:
            poped_val = stack.pop()
            if len(stack) != 0:
                area = arr[poped_val] * (i-stack[-1]-1)
            else:
                area = arr[poped_val] * i
            max_area = max(area, max_area)

    while stack:
        poped_val = stack.pop()
        if len(stack) != 0:
            area = arr[poped_val] * (i-stack[-1]-1)
        else:
            area = arr[poped_val] * i
        max_area = max(area, max_area)

    return max_area


def max_ractangle_area_in_mat(mat):
    if len(mat) == 0 or len(mat[0]) == 0 or mat is None:
        return 0

    max_area = histogram_area(mat[0])

    for row in range(1, len(mat)):
        for col in range(len(mat[0])):
            if mat[row][col]:
                mat[row][col] += mat[row-1][col]

        area = histogram_area(mat[row])
        max_area = max(area, max_area)

    return max_area

A = [[0, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 0, 0]]

print (max_ractangle_area_in_mat(A)) # Output: 9
