class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.DFS(grid, i, j)
                    island += 1
        return island

    def DFS(self, grid: List[List[str]], i, j):
        grid[i][j] = '0'
        i_dir = [1, -1, 0, 0]
        j_dir = [0, 0, 1, -1]
        i_len = len(grid)
        j_len = len(grid[0])

        for n in range(4):
            a = i + i_dir[n]
            b = j + j_dir[n]
            if a < i_len and a >= 0 and b < j_len and b >= 0 and grid[a][b] == '1':
                self.DFS(grid, a, b)

# Runtime: 84 ms, faster than 62.40% of Python3 online submissions for Number of Islands.
# Memory Usage: 14.1 MB, less than 42.33% of Python3 online submissions for Number of Islands.