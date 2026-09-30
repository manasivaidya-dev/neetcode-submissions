class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        idx = 0
        rows = len(board)
        cols = len(board[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        explore = []

        for i in range(0, rows):
            for j in range(0, cols):
                if board[i][j] == word[0]:
                    explore.append((i,j, 1, set([(i, j)])))
                    while explore:
                        i, j, idx, visited = explore.pop()
                        if idx == len(word):
                            return True
                        for xi, xj in directions:
                            ni = xi + i
                            nj = xj+j
                            if 0 <= ni < rows and 0 <= nj < cols and(ni, nj) not in visited  and board[ni][nj] == word[idx]:
                                new_visited = visited.copy()
                                new_visited.add((ni,nj))
                                explore.append((ni,nj, idx+1, new_visited))
        return False
        