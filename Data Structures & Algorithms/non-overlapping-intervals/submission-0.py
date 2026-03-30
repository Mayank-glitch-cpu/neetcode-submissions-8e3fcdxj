class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[1])
        end= intervals[0][1]
        overlap= 0

        for interval in intervals[1:]:
            if end<=interval[0]:
                end = interval[1]
            else:
                overlap+=1
        return overlap