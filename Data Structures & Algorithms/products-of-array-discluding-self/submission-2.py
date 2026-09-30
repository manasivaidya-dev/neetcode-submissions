class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        pref = 1
        for num in nums:
            prefix.append(pref)
            pref *= num
        suffix = [0] * len(nums)
        suff = 1
        for i in range(len(nums)-1,-1,-1):
            suffix[i] = suff
            suff *= nums[i]
        #print(suffix)
        answer = [0] * len(nums)
        for i in range(len(nums)):
            answer[i] = prefix[i]*suffix[i]
        return answer
        
        