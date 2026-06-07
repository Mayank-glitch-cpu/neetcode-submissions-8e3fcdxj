class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        write_index= 0

        for i in range(1, len(intervals)):
            if intervals[i][0] <= intervals[write_index][1]:
                intervals[write_index][1] = max(intervals[i][1], intervals[write_index][1])
            else:
                write_index+=1
                intervals[write_index]= intervals[i]
        print(intervals)
        print(write_index)
        del intervals[write_index + 1:]
        return intervals