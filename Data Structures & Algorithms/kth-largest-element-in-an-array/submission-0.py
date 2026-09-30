import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = []
        for num in nums:
            heapq.heappush(maxheap,-1*num)
        
        while k>1:
            heapq.heappop(maxheap)
            k -= 1
        return maxheap[0] * -1 
        