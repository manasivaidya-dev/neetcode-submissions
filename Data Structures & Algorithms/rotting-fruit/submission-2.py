class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()
        q = deque()
        mytime = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2 and (i,j) not in visited:
                    q.append((i,j,0))
                    visited.add((i,j))
        while q:
            ci,cj,time = q.popleft()
            mytime = max(mytime, time)
            for di, dj in directions:
                ni, nj = ci+di, cj+dj
                if 0<=ni<m and 0<=nj<n and (ni,nj) not in visited and grid[ni][nj] == 1:
                    q.append((ni,nj, time + 1))
                    visited.add((ni,nj))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    return -1
        return mytime


        