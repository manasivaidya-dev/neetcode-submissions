class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def recurse(explore_index, path):
    
            if explore_index == len(nums):
                app = path[:]
                answer.append(app)
                return
            else:
                path.append(nums[explore_index])
                recurse(explore_index + 1, path)
                path.pop()
                while explore_index + 1 < len(nums) and nums[explore_index] == nums[explore_index + 1]:
                    explore_index += 1
                recurse(explore_index + 1, path)
        nums.sort()
        recurse(0, [])
        return answer
        