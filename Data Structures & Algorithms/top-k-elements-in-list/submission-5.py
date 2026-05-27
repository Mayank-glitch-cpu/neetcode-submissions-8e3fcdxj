class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap= []
        freq= {}
        out=[]
        for num in nums:
            freq[num]= freq.get(num,0) +1

        for num,cnt in freq.items():
            heapq.heappush(max_heap,(-cnt, num))

        while k>0:
            cnt, num= heapq.heappop(max_heap)
            out.append(num)
            k-=1
        return out