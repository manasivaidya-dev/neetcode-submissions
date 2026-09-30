import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        coord_to_dist = {}
        for point in points:
            distance = math.sqrt((0 - point[0])**2 + (0 - point[1])**2)
            dist.append([distance, point[0], point[1]])
        heapq.heapify(dist)
        answer = []
        while len(dist) > 0:
            distance, x, y = heapq.heappop(dist)
            if len(answer) < k:
                answer.append([x,y])
        return answer
        
        