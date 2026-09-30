class Solution:
    def countones(self, n: int) -> int:
        count = 0
        for i in range(32):
            if(n & (1 << i)):
                count += 1
        return count
    def countBits(self, n: int) -> List[int]:
        nums = []
        for i in range (n+1):
            nums.append(self.countones(i))
        print(nums)
        return nums

        