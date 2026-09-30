import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        src_to_target = {}
        for i in range(1,n+1):
            src_to_target[i] = []
        for u,v,t in times:
            src_to_target[u].append((v,t))
        minheap = []
        heapq.heappush(minheap, (0,k))
        visited = set()
        time = [float('inf')] * (n+1) #only check 1 - n+1
        time[k] = 0

        while minheap:
            c_time, node = heapq.heappop(minheap)
            if node in visited:
                continue
            for neigh,weight in src_to_target[node]:
                new_time = c_time + weight
                if new_time < time[neigh]:
                    time[neigh] = new_time
                    heapq.heappush(minheap,(new_time, neigh))
        min_time = max(time[1:])
        if min_time == float('inf'):
            return -1
        else:
            return min_time

        
        