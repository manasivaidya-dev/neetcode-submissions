class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        rows, cols = len(grid), len(grid[0])

        dir = [[1,0], [0,1], [-1,0], [0,-1]]
        maxsize = 0
        size = 0

        def dfs(node) -> int:
            i,j = node
            size = 1
            for l,r in dir:
                ni, nj = i+l, j +r
                if ni >= 0 and ni < rows and nj >=0 and nj <cols and grid[ni][nj] == 1:
                    grid[ni][nj] =0
                    size += dfs((ni,nj))
            return size

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    size = dfs((r,c))
                    if size > maxsize :
                        maxsize = size
        return maxsize