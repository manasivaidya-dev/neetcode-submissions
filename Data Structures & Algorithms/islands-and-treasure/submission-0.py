class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j,0))
        #q has all treasure chests, now me move outward and 
        #populate all possible cells w minimum distance
        while q:
            ci, cj, cdist = q.popleft()
            for di, dj in directions:
                ni,nj = ci+di, cj+dj
                if 0 <= ni<rows and 0<=nj<cols and grid[ni][nj] != -1:
                    #check bounds and check its not water or chest
                    #cannot check for land bc we want to minimize
                    # land dist, so we take min of curr val and new val
                    if grid[ni][nj] > cdist+1:
                        grid[ni][nj] = cdist+1
                        q.append((ni,nj,cdist+1))
                    #only appending to q so neighbors
                    # have chance of being lower.
        