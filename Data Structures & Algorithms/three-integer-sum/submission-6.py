class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = set()
        for i in range(len(nums)):
            inverse = nums[i] * -1
            left, right = i+1, len(nums) - 1
            while left < right :
                threesum = nums[right] + nums[left]
                if threesum == inverse:
                    ans = [nums[right], nums[left], nums[i]]
                    answer.add(tuple(sorted(ans)))
                    left += 1
                    right -= 1
                elif threesum < inverse:
                    left += 1
                elif threesum > inverse:
                    right -= 1
        print(answer)
        return list(answer)