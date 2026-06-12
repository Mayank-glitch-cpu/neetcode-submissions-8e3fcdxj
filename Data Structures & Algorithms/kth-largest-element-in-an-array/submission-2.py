import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap =[]
        for num in nums:
            heapq.heappush(min_heap, -num)

        while k >0:
            out = - heapq.heappop(min_heap)
            k-=1

        return out
