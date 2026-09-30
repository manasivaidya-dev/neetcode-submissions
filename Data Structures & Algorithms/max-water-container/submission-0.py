class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            width =  right - left
            area = width * min(heights[left], heights[right])
            maxarea = max(area, maxarea)
            if heights[left]>= heights[right]:
                right -= 1
            else:
                left += 1
        return maxarea
        