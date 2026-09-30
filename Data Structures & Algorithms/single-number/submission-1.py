class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = res ^ num
        return res
        '''nums.sort()
        for i in range(0, len(nums) - 1, 2):
            print(i)
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[len(nums)-1]'''
        