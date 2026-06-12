import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res= []
        for num in nums:
            freq[num] = freq.get(num,0) + 1

        heap =[]

        for num, cnt in freq.items():
            heapq.heappush(heap, (-cnt, num))

        while k>0:
            cnt, num= heapq.heappop(heap)
            res.append(num)
            k-=1

        return res