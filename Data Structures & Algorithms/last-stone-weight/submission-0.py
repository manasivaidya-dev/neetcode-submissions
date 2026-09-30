import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-x for x in stones]
        heapq.heapify(neg_stones)

        while len(neg_stones)>1:
            print(neg_stones)
            x = heapq.heappop(neg_stones) * -1
            y = heapq.heappop(neg_stones) * -1
            if x != y:
                heapq.heappush(neg_stones, abs(x-y) * -1)

        if len(neg_stones) == 1:
            return neg_stones[0]*-1
        else:
            return 0
                
                
            
        