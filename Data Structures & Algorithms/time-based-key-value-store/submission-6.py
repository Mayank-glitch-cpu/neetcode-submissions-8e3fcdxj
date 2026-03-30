from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.time_set=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_set[key].append((value,timestamp)) # in value at index 1 we have time stamp
        print(self.time_set)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_set:
            return ""
        entries= self.time_set[key]
        print(entries)
        start,end= 0, len(entries)-1

        res= ""

        while start <=end:
            middle=(start+end)//2
            mid_value,mid_timestamp= entries[middle]
            if mid_timestamp== timestamp:
                return mid_value

            elif mid_timestamp< timestamp: # search in right 
                res= mid_value
                start= middle+1

            else:
                end= middle-1

        return res
            



