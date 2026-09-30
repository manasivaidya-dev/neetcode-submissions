class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        for i in range(len(nums)):
            thirdnum = nums[i]
            other_two_sum = -1 * nums[i]
            othernum_to_idx = {}
            for j in range(len(nums)):
                if i != j:
                    if nums[j] in othernum_to_idx:
                        secondnum = nums[othernum_to_idx[nums[j]]]
                        sorted_arr = sorted([thirdnum,nums[j], secondnum])
                        if thirdnum + nums[j] + secondnum == 0 and sorted_arr not in output:
                            output.append(sorted_arr)
                    else:
                        othernum = other_two_sum - nums[j]
                        othernum_to_idx[othernum] = j
        return output
