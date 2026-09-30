class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        othernum_to_numidx = {}
        for i in range(len(numbers)):
            if numbers[i] in othernum_to_numidx:
                return[othernum_to_numidx[numbers[i]], i+1]
            else:
                othernum = target - numbers[i]
                othernum_to_numidx[othernum] = i+1


        