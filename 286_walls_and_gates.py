class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        if (len(rooms) == 0):
            return
        # solve this question using BFS
        queue = collections.deque()
        i_dir = [1, -1, 0, 0]
        j_dir = [0, 0, 1, -1]
        i_len = len(rooms)
        j_len = len(rooms[0])

        # use brute force to find all the gate
        for i in range(i_len):
            for j in range(j_len):
                if rooms[i][j] == 0:
                    queue.append([i, j])

        # then iterate all the gate to apply BFS
        while len(queue) != 0:
            cur = queue.popleft()
            i, j = cur[0], cur[1]

            for x in range(4):
                a = i + i_dir[x]
                b = j + j_dir[x]
                if a < i_len and a >= 0 and b < j_len and b >= 0:
                    if rooms[a][b] == 2147483647:
                        queue.append([a, b])
                        rooms[a][b] = rooms[i][j] + 1

