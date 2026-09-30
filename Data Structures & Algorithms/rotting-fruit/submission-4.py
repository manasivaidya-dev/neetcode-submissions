class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited= set()
        tmax = 0
        dir = [[0,1], [1,0], [0,-1], [-1, 0]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c,0))
                    visited.add((r,c))
        while q:
            i, j, time = q.popleft()
            tmax = max (time, tmax)
            for l,r in dir:
                ni, nj = i+l, j +r
                if ni >= 0 and ni < rows and nj >= 0 and nj <cols and (ni,nj) not in visited:
                    if grid[ni][nj] == 1:
                        q.append((ni,nj, time + 1))
                        visited.add((ni,nj))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    return -1
        return tmax