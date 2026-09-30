from typing import List, Tuple
class Solution:
    def findcut(self, nums: List[int]) -> Tuple[int, int]:
        high =  len(nums) - 1
        low = 0
        while high >= low:
            mid = (high + low)//2
            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return (mid, mid+1)
            elif nums[mid] >= nums[0]:
                low = mid + 1
            else:
                high = mid - 1
        return (0,0)
        
    def search(self, nums: List[int], target: int) -> int:
        arr_size = len(nums) - 1
        cut = self.findcut(nums)
        print(cut)
        if target <= nums[arr_size]:
            low = cut[1]
            high = arr_size
        else:
            low = 0
            high = cut[0]
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

        