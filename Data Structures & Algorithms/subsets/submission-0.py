class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def recurse(indices_seen, path):
            if indices_seen == len(nums):
                answer.append(path[:]) #apped a copy so changes are not propagated
                return
            else:
                path.append(nums[indices_seen])
                recurse(indices_seen + 1, path)
                path.pop()
                recurse(indices_seen + 1,  path)
        recurse(0, [])
        return answer



        