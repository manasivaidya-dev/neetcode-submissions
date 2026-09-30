"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        elif len(intervals) == 1:
            return 1
        intervals.sort(key = lambda x:x.start)
        room_to_endtime = {}
        room_to_endtime[1] = intervals[0].end
        for i in range(1,len(intervals)):
            newroom = True
            for room, endtime in room_to_endtime.items():
                if intervals[i].start >= endtime:
                    room_to_endtime[room] = intervals[i].end
                    newroom = False
                    break
            if newroom:
                room_num = len(room_to_endtime) + 1
                room_to_endtime[room_num] = intervals[i].end
        return len(room_to_endtime)

#key value
#1, 40
#1:40, 2:10
#1:40, 2:20
        
        