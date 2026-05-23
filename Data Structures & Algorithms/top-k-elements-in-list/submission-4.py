import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap= []
        out= []
        freq= {}
        for num in nums:
            freq[num]= freq.get(num,0) +1

        for num, cnt in freq.items():
            heapq.heappush(heap, (-cnt, num))

        while k>0:
            freq, num = heapq.heappop(heap)
            out.append(num)
            k-=1  
        return out