# LC51. N-Queens
# https://leetcode.com/problems/n-queens/
# place N queens so that none of the queen attacks each other in NxN chess board
# 
# Reference
# https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/
# https://www.youtube.com/watch?v=jJPtLzq1E-Y


def is_safe(row, col, queens):
    for queen in queens[:-1]:
        r = queen[0]
        c = queen[1]

        if r == row:
            return False

        if abs(r-row) == abs(c-col):
            return False

    return True



def place_queens(n, col, queens):
    if col >= n:
        return True

    row = 0

    while row < n:
        queens.append((row, col))
        if is_safe(row, col, queens) and place_queens(n, col+1, queens):
            return True
        queens.pop()
        row += 1

    return False



def n_queens(n):
    if n < 0:
        return []

    queens = []

    if place_queens(n, 0, queens):
        return queens

    return []


print (n_queens(2)) # returns []
print (n_queens(4)) # returns [(1, 0), (3, 1), (0, 2), (2, 3)]
