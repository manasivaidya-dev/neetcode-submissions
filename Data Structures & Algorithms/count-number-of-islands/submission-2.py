from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        rows, cols = len(grid), len(grid[0])

        dir = [[1,0], [0,1], [-1,0], [0,-1]]
        num = 0
        q = deque()
        def dfs(node):
            q.append(node)
            while q:
                i,j = q.pop()
                for l,r in dir:
                    ni, nj = i+l, j +r
                    if ni >= 0 and ni < rows and nj >=0 and nj <cols and grid[ni][nj] == "1":
                        grid[ni][nj] ="0"
                        q.append((ni,nj))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num += 1
                    grid[r][c] = "0"
                    dfs((r,c))
        return num