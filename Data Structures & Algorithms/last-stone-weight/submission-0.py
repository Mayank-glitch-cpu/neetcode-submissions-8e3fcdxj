import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def heapify(nums): # fucntion to make max heap
            max_heap= [-num for num in nums]
            heapq.heapify(max_heap)
            return max_heap

        stones= heapify(stones)
        while len(stones)>1:
            x= - heapq.heappop(stones)
            y= - heapq.heappop(stones)
            if x==y:
                continue
            else:
                heapq.heappush(stones,-(abs(x-y)))
        if stones:
            return -stones[0]
        else:
            return 0
