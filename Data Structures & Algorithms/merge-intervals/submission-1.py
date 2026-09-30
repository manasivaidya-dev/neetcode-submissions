class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        answer = [intervals[0]]

        for first, second in intervals[1:]:
            lastitem_secondval  = answer[-1][1]
            if lastitem_secondval >= first:
                answer[-1][1] = max(lastitem_secondval, second)
            else:
                answer.append([first,second])
        return answer
        