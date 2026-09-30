class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(nums)
        longest = 0
        curr_run = 1
        for i in range(len(nums) - 1):
            if sorted_nums[i+1] == sorted_nums[i]:
                continue
            elif sorted_nums[i+1] - 1 == sorted_nums[i]:
                curr_run +=1
            else:
                longest = max(longest, curr_run)
                curr_run = 1
        longest = max(longest, curr_run)
        return longest
        