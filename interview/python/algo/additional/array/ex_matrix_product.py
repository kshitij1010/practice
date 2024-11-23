# Given a matrix, find the path from top left to bottom right with the greatest product by moving only down and right.
# Example,
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
#
# 1 -> 4 -> 7 -> 8 -> 9
# 2016
#
# [-1, 2, 3]
# [4, 5, -6]
# [7, 8, 9]
#
# -1 -> 4 -> 5 -> -6 -> 9
# 1080
#
# Reference:
# https://www.byte-by-byte.com/matrixproduct/


def matrix_product_max_path(mat):
    if mat is None:
        return 0
    row_size = len(mat)
    col_size = len(mat[0])
    product_max = [ [0] * col_size for i in range(row_size)]
    product_min = [ [0] * col_size for i in range(row_size)]


    for i in range(row_size):
        for j in range(col_size):
            max_val = float('-inf')
            min_val = float('inf')

            if i==0 and j==0:
                max_val = mat[i][j]
                min_val = mat[i][j]

            if i > 0:
                temp_max_val = max(mat[i][j]*product_max[i-1][j], mat[i][j]*product_min[i-1][j])
                max_val = max(max_val, temp_max_val)
                temp_min_val = min(mat[i][j]*product_max[i-1][j], mat[i][j]*product_min[i-1][j])
                min_val = min(min_val, temp_min_val)

            if j > 0:
                temp_max_val = max(mat[i][j]*product_max[i][j-1], mat[i][j]*product_min[i][j-1])
                max_val = max(max_val, temp_max_val)
                temp_min_val = min(mat[i][j]*product_max[i][j-1], mat[i][j]*product_min[i][j-1])
                min_val = min(min_val, temp_min_val)

            product_max[i][j] = max_val
            product_min[i][j] = min_val
    print (product_max)
    return product_max[row_size-1][col_size-1]


mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print (matrix_product_max_path(mat1))
# Output: 2016

mat2 = [[-1, 2, 3], [4, 5, -6], [7, 8, 9]]
print (matrix_product_max_path(mat2))
# Output: 1080
