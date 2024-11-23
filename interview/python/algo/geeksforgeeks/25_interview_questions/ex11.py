# Print a given matrix in spiral form

# https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/

def print_row(mat, row, col_start, col_end):
    for j in range(col_start, col_end+1):
        print (mat[row][j], end=" ")

def print_col(mat, col, row_start, row_end):
    for i in range(row_start, row_end+1):
        print (mat[i][col], end=" ")

def print_row_rev(mat, row, col_start, col_end):
    for j in range(col_start, col_end-1, -1):
        print (mat[row][j], end=" ")

def print_col_rev(mat, col, row_start, row_end):
    for i in range(row_start, row_end-1, -1):
        print (mat[i][col], end=" ")


def print_in_spiral(mat):
    if len(mat) == 0 and mat is None:
        print ([])

    if len(mat) == 1:
        print (mat)

    row_start = 0
    col_start = 0
    row_end = len(mat) - 1
    col_end = len(mat[0]) - 1


    while row_start <= row_end and col_start <= col_end:
        print_row(mat, row_start, col_start, col_end)
        row_start += 1

        print_col(mat, col_end, row_start, row_end)
        col_end -= 1

        if row_start <= row_end:
            print_row_rev(mat, row_end, col_end, col_start)
            row_end -= 1

        if col_start <= col_end:
            print_col_rev(mat, col_start, row_end, row_start)
            col_start += 1

    return


mat1 = [[1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18]]
print_in_spiral(mat1)
