# Link: https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        island = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    island += 1

        return island


    def dfs(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '0':
            return

        grid[row][col] = '0'
        for r, c in [(row-1, col), (row, col+1), (row+1, col), (row, col-1)]:
            self.dfs(grid, r, c)

        return
