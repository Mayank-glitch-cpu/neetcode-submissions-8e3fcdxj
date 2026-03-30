class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start , end= newInterval[0], newInterval[1]
        out= []
        inserted = False
        for interval in intervals:
            if end < interval[0]:
                if not inserted:
                    out.append([start, end])
                    inserted = True
                out.append(interval)
            elif start > interval[1]:
                out.append(interval)
            else:
                start, end = min(start, interval[0]), max(end, interval[1])
        
        if not inserted:
            out.append([start, end])

        return out