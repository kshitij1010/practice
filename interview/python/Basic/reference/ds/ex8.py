# 8. Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to O.
# # 

def make_row_zero(mat, row, col_len):
    for j in range(col_len):
        mat[row][j] = 0


def make_col_zero(mat, column, row_len):
    for i in range(row_len):
        mat[i][column] = 0

def zeroMatrix(mat):
    rows = len(mat)
    columns = len(mat[0])

    first_row_zero = False
    first_col_zero = False

    for i in range(rows):
        for j in range(columns):
            if mat[i][j] == 0:
                if i == 0 and j == 0:
                    first_row_zero = True
                    first_col_zero = True
                elif i == 0:
                    first_row_zero = True
                elif j == 0:
                    first_col_zero = True
                else:
                    mat[i][0] = 0
                    mat[0][j] = 0

    # make rows zero
    for i in range(1, rows):
        if mat[i][0] == 0:
            make_row_zero(mat, i, columns)

    # make columns zero
    for j in range(1, columns):
        if mat[0][j] == 0:
            make_col_zero(mat, j, rows)

    if first_row_zero:
        make_row_zero(mat, 0, columns)
        
    if first_col_zero:
        make_col_zero(mat, 0, rows)

    return mat



data = [
    {
        "input": [  [[0, 1, 2],
                     [3, 4, 5],
                     [6, 7, 8],] ],
        "output": [ [0, 0, 0],
                    [0, 4, 5],
                    [0, 7, 8], ],
    },
    {
        "input": [  [[0, 1, 2],
                     [3, 0, 5],
                     [6, 7, 8],]],
        "output": [ [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 8],],
    },
    {
        "input": [  [[1,0,1,2],
                     [2,8,2,1],
                     [0,2,3,4],
                     [2,5,7,16]]],
        "output": [ [0,0,0,0],
                    [0,0,2,1],
                    [0,0,0,0],
                    [0,0,7,16]]
    },
    {
        "input": [  [[1,2,3,4],
                     [5,6,0,8],
                     [0,10,11,12],
                     [13,14,15,16]]],
        "output": [ [0,2,0,4],
                    [0,0,0,0],
                    [0,0,0,0],
                    [0,14,0,16]]
    }
]


from helper import Test
test = Test()
test.check(zeroMatrix, data)
