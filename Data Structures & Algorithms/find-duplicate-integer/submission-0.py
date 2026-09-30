class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1 2 3 1 1
        # 0 1 2 3 4
        fast = 0
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        
        slow_again = 0
        while slow != slow_again:
            slow =  nums[slow]
            slow_again = nums[slow_again]
        return slow