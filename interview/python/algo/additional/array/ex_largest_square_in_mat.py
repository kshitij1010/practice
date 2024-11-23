# largest square of 1's in 2d matrix
# example,
# 1 1 0 1 0
# 0 1 1 1 0
# 1 1 1 1 0
# 0 1 1 1 0
# output: 3 (since 3X3 is the largest square in this matrix)


def largest_square_size(mat):
    S = mat
    row_size = len(mat)
    col_size = len(mat[0])

    square_size = 0

    for i in range(row_size):
        for j in range(col_size):
            if i > 0 and j > 0 and mat[i][j] > 0:
                S[i][j] = min(S[i][j-1], S[i-1][j-1], S[i-1][j]) + 1
                square_size = max(square_size, S[i][j])

    return square_size

mat = [
        [1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [0, 1, 1, 1, 0]
]

print (largest_square_size(mat))

mat1 = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
]

print (largest_square_size(mat1))
