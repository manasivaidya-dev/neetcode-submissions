class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, len(height) - 1
        trapped = 0
        lmax = 0
        rmax = 0
        while left < right:
            if height[left] <height[right]:
                left += 1
                lmax = max(height[left -1],  lmax)
                if (lmax - height[left - 1])>  0:
                    trapped += lmax - height[left - 1]
            else:
                right -= 1
                rmax = max(height[right +1],  rmax)
                if (rmax - height[right + 1])>  0:
                    trapped += rmax - height[right + 1]
        return trapped
                


        '''
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
        return trapped'''


        