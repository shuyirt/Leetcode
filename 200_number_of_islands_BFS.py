class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if (len(grid) == 0):
            return 0

        # solve this question using BFS
        queue = collections.deque()
        i_dir = [1, -1, 0, 0]
        j_dir = [0, 0, 1, -1]
        i_len = len(grid)
        j_len = len(grid[0])
        island = 0

        # iterate every node to ensure each node is added
        for i in range(i_len):
            for j in range(j_len):
                if grid[i][j] == '1':
                    island += 1
                    queue.append([i, j])
                    grid[i][j] = '0'
                    while len(queue) != 0:
                        cur = queue.popleft()
                        x, y = cur[0], cur[1]
                        for n in range(4):
                            a = x + i_dir[n]
                            b = y + j_dir[n]
                            if a < i_len and a >= 0 and b < j_len and b >= 0:
                                if grid[a][b] == '1':
                                    grid[a][b] = '0'
                                    queue.append([a, b])
        return island

# Runtime: 68 ms, faster than 91.50% of Python3 online submissions for Number of Islands.
# Memory Usage: 13.6 MB, less than 91.18% of Python3 online submissions for Number of Islands.