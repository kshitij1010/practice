# 7. Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
# write a method to rotate the image by 90 degrees.
# can you do this in place?


def transpose(mat):
    for i in range(len(mat)):
        for j in range(i, len(mat)):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    return mat

def reverseRows(mat):
    for i in range(len(mat)):
        for j in range(len(mat)//2):
            mat[i][j], mat[i][len(mat)-j-1] = mat[i][len(mat)-j-1], mat[i][j]
    return mat

# Counterclockwise
def rotateMatrixAntiClockWise(mat):
    if mat is None:
        return None

    row_len = column_len = len(mat)

    for i in range(row_len//2):
        for j in range(i, column_len-i-1):
            temp = mat[i][j]
            mat[i][j] = mat[j][column_len-i-1]
            mat[j][column_len-i-1] = mat[column_len-i-1][column_len-j-1]
            mat[column_len-i-1][column_len-j-1] = mat[column_len-j-1][i]
            mat[column_len-j-1][i] = temp

    return mat

# Counterclockwise using ( orig -> reverse each row -> transporse)
def rotateMatrixAntiClockWise2(mat):
    reverseRows(mat)
    transpose(mat)
    return mat



# Clockwise
def rotateMatrixClockWise(mat):
    row = col = len(mat)
    for i in range(row//2):
        for j in range(i, col-i-1):
            temp = mat[i][j]            
            mat[i][j] = mat[col-j-1][i]
            mat[col-j-1][i] = mat[col-i-1][col-j-1]
            mat[col-i-1][col-j-1] = mat[j][col-i-1]
            mat[j][col-i-1] = temp

    return mat



# Clockwise using ( orig -> transporse -> reverse each row)
def rotateMatrixClockWise2(mat):
    transpose(mat)
    mat = reverseRows(mat)
    return mat



dataAntiClockwise = [
    {
        "input": [ [[1,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12],
                    [13,14,15,16]]],
        "output":  [[4, 8, 12, 16],
                    [3, 7, 11, 15],
                    [2, 6, 10, 14],
                    [1, 5, 9, 13]]
    }
]

dataAntiClockwise2 = [
    {
        "input": [ [[1,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12],
                    [13,14,15,16]]],
        "output":  [[4, 8, 12, 16],
                    [3, 7, 11, 15],
                    [2, 6, 10, 14],
                    [1, 5, 9, 13]]
    }
]

dataClockwise = [
    {
        "input": [ [[1,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12],
                    [13,14,15,16]]],
        "output":  [[13,9,5,1],
                    [14,10,6,2],
                    [15,11,7,3],
                    [16,12,8,4]]
    }
]

dataClockwise2 = [
    {
        "input": [ [[1,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12],
                    [13,14,15,16]]],
        "output":  [[13,9,5,1],
                    [14,10,6,2],
                    [15,11,7,3],
                    [16,12,8,4]]
    }
]


from helper import Test
test = Test()
test.check(rotateMatrixAntiClockWise, dataAntiClockwise)
test.check(rotateMatrixAntiClockWise2, dataAntiClockwise2)
test.check(rotateMatrixClockWise, dataClockwise)
test.check(rotateMatrixClockWise2, dataClockwise2)
