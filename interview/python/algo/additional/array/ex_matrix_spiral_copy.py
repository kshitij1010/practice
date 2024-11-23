# Given a 2D array (matrix) inputMatrix of integers,
# create a function spiralCopy that copies inputMatrix’s values into a 1D array in a spiral order, clockwise.
# Your function then should return that array.
# Analyze the time and space complexities of your solution.
#
# Example,
# input:  inputMatrix  = [ [1,    2,   3,  4,    5],
#                          [6,    7,   8,  9,   10],
#                          [11,  12,  13,  14,  15],
#                          [16,  17,  18,  19,  20] ]
#
# output: [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]



def spiral_copy(inputMatrix):
    if len(inputMatrix) < 2 and len(inputMatrix[0]) < 2 or inputMatrix is None:
        return [inputMatrix[0][0]]

    if len(inputMatrix) == 1:
        return inputMatrix[0]

    if len(inputMatrix[0]) == 1:
        res = []
        for row in range(len(inputMatrix)):
            res.append(inputMatrix[row][0])
        return res

    row_start = 0
    row_end = len(inputMatrix) - 1

    col_start = 0
    col_end = len(inputMatrix[0]) -1

    res = []

    while row_start <= row_end and col_start <= col_end:
        for col in range(col_start, col_end+1):
            res.append(inputMatrix[row_start][col])
        row_start += 1

        for row in range(row_start, row_end+1):
            res.append(inputMatrix[row][col_end])
        col_end -= 1

        if row_start > row_end: break
        for col in range(col_end, col_start-1, -1):
            res.append(inputMatrix[row_end][col])
        row_end -= 1

        if col_start > col_end: break
        for row in range(row_end, row_start-1, -1):
            res.append(inputMatrix[row][col_start])
        col_start += 1

    return res




print (spiral_copy([[1]])) # [1]
print (spiral_copy([[1],[2]])) # [1, 2]
print (spiral_copy([[1,2]])) # [1, 2]
print (spiral_copy([[1,2],[3,4]])) # [1, 2, 4, 3]
print (spiral_copy([[1,2,3,4,5],[6,7,8,9,10]])) # [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]
print (spiral_copy([[1,2,3,4,5],
                    [6,7,8,9,10],
                    [11,12,13,14,15],
                    [16,17,18,19,20]])) # [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]

print (spiral_copy([[1,2,3,4],[5,6,7,8],[9,10,11,12]])) # [1,2,3,4,8,12,11,10,9,5,6,7]
