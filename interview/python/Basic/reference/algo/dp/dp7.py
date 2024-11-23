# Number of Paths in Matrix
# You’re testing a new driverless car that is located at the Southwest (bottom-left) corner of an n×n grid.
# The car is supposed to get to the opposite, Northeast (top-right), corner of the grid. Given n, the size of the grid’s axes,
# write a function numOfPathsToDest that returns the number of the possible paths the driverless car can take.
#
# The car must abide by the following two rules: it cannot cross the diagonal border.
# In other words, in every step the position (i,j) needs to maintain i >= j.
# See the illustration above for n = 5.
# In every step, it may go one square North (up), or one square East (right), but not both.
# E.g. if the car is at (3,1), it may go to (3,2) or (4,1).
#
# example,
# Given matrix
# 1 0 0 0
# 0 0 0 0
# 0 0 0 0
# 0 0 0 9
#
# Find the path to reach from 9 to 1 or 1 to 9 using area as follow. (- is blocked area)
# 1 - - -
# 0 0 - -
# 0 0 0 -
# 0 0 0 9

def num_of_paths_to_dest(n):
    mat = [[0] * n for i in range(n)]
    mat[0][0] = 1
    for i in range(1,n):
        for j in range(n):
            if i >= j:
                if j == 0:
                    mat[i][j] = mat[i-1][j]
                else:
                    mat[i][j] = mat[i-1][j] + mat[i][j-1]
    return mat[n-1][n-1]

n = 1
print (num_of_paths_to_dest(n))
n = 2
print (num_of_paths_to_dest(n))
n = 3
print (num_of_paths_to_dest(n))
n = 4
print (num_of_paths_to_dest(n))
n = 5
print (num_of_paths_to_dest(n))
n = 6
print (num_of_paths_to_dest(n))


################## Another similar example #####################
# Count number of ways to reach destination in a Maze
# Given a maze with obstacles,
# count number of paths to reach rightmost-bottommost cell from topmost-leftmost cell.
# A cell in given maze has value -1 if it is a blockage or dead end, else 0.
# https://www.geeksforgeeks.org/count-number-ways-reach-destination-maze/


def num_of_paths_to_dest_with_blocks(mat):
    paths = [[0]*len(mat[0]) for _ in range(len(mat))]
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if mat[row][col] != -1:
                if row == 0 and col == 0:
                    paths[row][col] = 1
                elif row == 0:
                    paths[row][col] = paths[row][col-1]
                elif col == 0:
                    paths[row][col] = paths[row-1][col]
                else:
                    paths[row][col] = paths[row][col-1] + paths[row-1][col]
    return paths[-1][-1]



# find the ways to get to value 9 in the matrix from top-left
def find_ways(mat):
    row = 0
    col = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 9:
                row = i
                col = j
                break

    new_mat = [mat[i][:col+1] for i in range(row+1)]
    return num_of_paths_to_dest_with_blocks(new_mat)


maze = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [-1, 0, 0, 0],
        [0, 0, 0, 9 ]]

print ("Num of ways with blocks:", num_of_paths_to_dest_with_blocks(maze))


print ("Find ways:", find_ways(maze))
