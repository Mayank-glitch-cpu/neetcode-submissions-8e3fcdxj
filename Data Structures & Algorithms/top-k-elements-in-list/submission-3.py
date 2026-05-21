import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num]= freq.get(num,0) +1
        print(freq)
        heap= []

        for num, cnt in freq.items():
            heapq.heappush(heap, (-cnt,num))
        
        out = []

        while heap:
            cnt,num= heapq.heappop(heap)
            out.append(num)
            if len(out)>=k:
                return out