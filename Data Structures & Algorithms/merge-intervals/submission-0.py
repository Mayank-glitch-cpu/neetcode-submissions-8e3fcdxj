class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start, end= intervals[0][0], intervals[0][1]
        out=[]
        for i in range(1, len(intervals)):
            if end < intervals[i][0]:
                out.append([start,end])
                start, end = intervals[i][0], intervals[i][1]
            else:
                start, end= min(start, intervals[i][0]), max(end, intervals[i][1])

        out.append([start, end])
        return out