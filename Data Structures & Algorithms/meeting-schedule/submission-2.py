"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        intervals.sort(key = lambda x:x.start) #sorting based on start time
        prev_interval = intervals[0]

        for i in range(1,len(intervals)):
            if intervals[i].start < prev_interval.end:
                return False
            prev_interval = intervals[i]
        return True
