class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        atlantic = set()
        pacific = set()
        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    pacific.add((i,j))
                if i == rows-1 or j == cols - 1:
                    atlantic.add((i,j))
        def bfs(currset, solnset):
            q = deque(currset)
            solnset.update(currset)
            while q:
                ci,cj= q.popleft()
                for di,dj in directions:
                    ni,nj = di+ci,dj+cj
                    if 0<=ni<rows and 0<=nj<cols and (ni,nj) not in solnset and heights[ni][nj] >= heights[ci][cj]:
                        q.append((ni,nj))
                        solnset.add((ni,nj)) 
        pacificsoln = set()
        atlsoln = set()
        bfs(pacific, pacificsoln)
        bfs(atlantic, atlsoln)
        answer = []
        while atlsoln:
            i,j = atlsoln.pop()
            if (i,j) in pacificsoln:
                answer.append([i,j]) 
        return answer
        