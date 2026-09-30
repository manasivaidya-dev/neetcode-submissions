class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_appeared = {}
        for num in nums:
            if num in has_appeared:
                return True
            else:
                has_appeared[num] = 1
        return False
         