from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def finish(k):
            count = 0
            for pile in piles:
                count += ceil(pile/k)
            if count <= h:
                return True
            else:
                return False
        high = 0
        for pile in piles:
            if pile > high:
                high = pile
        low = 1
        while low < high:
            mid = (low+high)//2
            if finish(mid):
                high = mid
            else:
                low = mid + 1
        return low
        
        

            

        