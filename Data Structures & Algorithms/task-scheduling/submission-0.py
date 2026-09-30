import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_to_freq = {}
        for task in tasks:
            if task not in task_to_freq:
                task_to_freq[task] = 1
            else:
                task_to_freq[task] += 1
        maxheap = [-x for x in task_to_freq.values()]
        heapq.heapify(maxheap)
        time = 0
        q = deque() #[count, time]
        while q or maxheap:
            time += 1
            if maxheap:
                recent = 1 + heapq.heappop(maxheap)
                if recent < 0:
                    q.append([recent, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
        return time
        