import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return 0
        heap= []
        for num in nums:
            heapq.heappush(heap, -num)

        while k>0:
            out= heapq.heappop(heap)
            k-=1
        return -out