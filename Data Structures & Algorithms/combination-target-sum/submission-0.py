class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []

        def recurse(explore, path, sum_so_far):
            if sum_so_far == target:
                answer.append(path[:])
                return
            if len(nums) == explore or sum_so_far > target:
                return
            path.append(nums[explore])
            recurse(explore, path, sum_so_far + nums[explore])
            path.pop()
            recurse(explore + 1, path, sum_so_far)
        recurse(0, [],  0)
        return answer
        