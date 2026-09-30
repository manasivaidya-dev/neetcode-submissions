class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxl = [0] *n
        maxr = [0] *n
        for i in range(1,n):
           maxl[i] = max(maxl[i-1], height[i-1])
        for i in range(n-2, -1,-1):
           maxr[i] = max(maxr[i+1], height[i+1])
        trapped = 0
        for i in range(0, len(height)):
            water = min(maxl[i], maxr[i]) - height[i]
            if water > 0:
                trapped += water
        return trapped


        