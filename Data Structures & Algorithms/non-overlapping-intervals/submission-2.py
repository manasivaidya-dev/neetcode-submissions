class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i:i[1])
        #intervals[i][1] <= intervals[i+1][0]
        #intervals[i][0] >= intervals[i-1][1]

        #[[1,2],[3,5],[4,8],[8,10],[12,16]]
        print(intervals)
        prevEnd = intervals[0][1]
        count = 0
        for i in range (1, len(intervals)):
            if prevEnd <= intervals[i][0]:
                prevEnd = intervals[i][1]
            else:
                count += 1
        return count
        