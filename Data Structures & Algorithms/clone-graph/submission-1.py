from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}
        visited[node]= Node(node.val)
        q = deque()
        q.append(node)
        while q:
            n = q.popleft()
            copy = visited[n]
            if not n.neighbors:
                copy.neighbors = []
            else:
                copy.neighbors = []
                for neigh in n.neighbors:
                    if neigh not in visited:
                        visited[neigh] = Node(neigh.val)
                        q.append(neigh)
                    copy.neighbors.append(visited[neigh])
        return visited[node]


        