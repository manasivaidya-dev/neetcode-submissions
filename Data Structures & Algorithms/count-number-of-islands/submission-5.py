from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        q = deque()
        num_islands = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    visited.add((i,j))
                    q.append((i,j))
                    while q:
                        row,col = q.popleft()
                        for dr, dc in directions:
                            ni, nj = row + dr, col + dc
                            if ni >= 0 and ni < rows and nj >= 0 and nj < cols and grid[ni][nj] == "1" and (ni,nj) not in visited:
                                visited.add((ni,nj))
                                q.append((ni,nj))
                    num_islands += 1
        return num_islands
