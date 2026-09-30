class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            answer[i] *= prefix
            prefix *= nums[i]
        print(answer)
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            answer[i] *= suffix
            suffix *= nums[i]
        print(answer)
        return answer

        