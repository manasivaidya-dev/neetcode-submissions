class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()
        q = deque()
        rows = len(grid)
        cols=len(grid[0])
        max_area = 0

        for i in range(0,rows):
            for j in range(0,cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    q.append((i,j))
                    visited.add((i,j))
                    area = 0
                    while q:
                        i,j = q.popleft()
                        area += 1 
                        for di, dj in directions:
                            ni = i+di
                            nj = j +dj
                            if 0 <= ni <rows and 0<= nj < cols and grid[ni][nj] == 1 and (ni,nj) not in visited:
                                q.append((ni,nj))
                                visited.add((ni,nj))
                    max_area = max(max_area, area)
        return max_area



        