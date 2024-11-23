# LC200. Number of Islands
# https://leetcode.com/problems/number-of-islands/
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


def mark_visited(binaryMatrix, row, col):
    if row < 0 or col < 0 or row >= len(binaryMatrix) or col >= len(binaryMatrix[0]) or binaryMatrix[row][col] == 0:
        return

    binaryMatrix[row][col] = 0
    mark_visited(binaryMatrix, row-1, col)
    mark_visited(binaryMatrix, row+1, col)
    mark_visited(binaryMatrix, row, col-1)
    mark_visited(binaryMatrix, row, col+1)

    return

def get_number_of_islands(binaryMatrix):
    island_count = 0

    for i in range(len(binaryMatrix)):
        for j in range(len(binaryMatrix[0])):
            if binaryMatrix[i][j]:
                mark_visited(binaryMatrix, i, j)
                island_count += 1

    return island_count


binaryMatrix = [ [0,    1,    0,    1,    0],
                 [0,    0,    1,    1,    1],
                 [1,    0,    0,    1,    0],
                 [0,    1,    1,    0,    0],
                 [1,    0,    1,    0,    1] ]

print (get_number_of_islands(binaryMatrix))
