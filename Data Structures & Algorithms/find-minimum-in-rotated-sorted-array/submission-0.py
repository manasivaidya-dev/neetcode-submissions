class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while high >= low:
            mid = (high + low)//2
            if mid < high and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if mid > low and nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[0]:
                low = mid + 1
            else:
                high = mid - 1
        return nums[0]
        