class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {} #num -> idx of the value that would need to be added to make target
        for i in range(len(nums)):
            if nums[i] in num_to_idx:
                return [num_to_idx[nums[i]], i]
            else:
                num_needed = target - nums[i]
                num_to_idx[num_needed] = i

        