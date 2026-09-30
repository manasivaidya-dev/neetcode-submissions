class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[1]:
                result.append(newInterval)
                return result + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
            else: #merging case intervals[i][1] = newInterval[0]
                start = min(intervals[i][0], newInterval[0])
                end = max(intervals[i][1], newInterval[1])
                newInterval = [start, end]
        result.append(newInterval)
        return result

        