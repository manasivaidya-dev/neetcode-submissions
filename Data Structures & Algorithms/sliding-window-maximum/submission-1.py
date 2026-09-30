class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxheap = []
        answer = []
        for i in range(0, len(nums)):
            heapq.heappush(maxheap, [-nums[i], i])
            if i >= k - 1: #we have looked at k elemnts
                while maxheap[0][1] <= (i - k):
                    heapq.heappop(maxheap)
                answer.append(-maxheap[0][0])
        return answer
                


        '''right, left = 0,0
        while k > (right - left + 1):
            right += 1
        answer = []


        while right < len(nums):
            maxheap = [-x for x in nums[left:right+1]]
            heapq.heapify(maxheap)
            answer.append(-(heapq.heappop(maxheap)))
            right += 1
            left += 1
        return answer'''


        