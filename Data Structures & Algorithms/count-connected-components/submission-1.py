from collections import defaultdict, deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjlist = defaultdict(set)
        for e in edges:
            adjlist[e[0]].add(e[1])
            adjlist[e[1]].add(e[0])
        visited = set()
        components = 0
        def dfs(vals:set):
            for val in vals:
                if val in visited:
                    continue
                visited.add(val)
                dfs(adjlist[val])

        for key, vals in adjlist.items():
            if key not in visited:
                visited.add(key)
                components += 1
                dfs(vals)
        
        if len(adjlist) < n :
            components += n - len(adjlist)
        return components

        


        