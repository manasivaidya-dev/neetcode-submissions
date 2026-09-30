class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxarea = 0
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i,j))
                    grid[i][j] = 0
                    area = 0
                    while q:
                        ci,cj = q.popleft()
                        area += 1
                        for di, dj in directions:
                            ni, nj = di+ci, dj+cj
                            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                                q.append((ni,nj))
                                grid[ni][nj] = 0
                    maxarea = max(area,maxarea)
        return maxarea
        