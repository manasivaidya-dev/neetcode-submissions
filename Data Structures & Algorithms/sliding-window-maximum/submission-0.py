class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        right, left = 0,0
        while k > (right - left + 1):
            right += 1
        answer = []


        while right < len(nums):
            maxheap = [-x for x in nums[left:right+1]]
            heapq.heapify(maxheap)
            answer.append(-(heapq.heappop(maxheap)))
            right += 1
            left += 1
        return answer


        