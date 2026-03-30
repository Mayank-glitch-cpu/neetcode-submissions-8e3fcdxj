class MedianFinder:

    def __init__(self):
        self.small_heap=[]
        self.large_heap=[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_heap,-num)
        if self.small_heap and self.large_heap and (-self.small_heap[0] >self.large_heap[0]):
                push=-heapq.heappop(self.small_heap)
                heapq.heappush(self.large_heap,push)
        if len(self.small_heap)>len(self.large_heap)+1:
            push=-heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap,push)
        elif len(self.large_heap)>len(self.small_heap)+1:
            push=heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap,-push)


    def findMedian(self) -> float:
        if len(self.small_heap) == len(self.large_heap):
            return ((-self.small_heap[0] +self.large_heap[0])/2)
        else:
            if len(self.small_heap)>len(self.large_heap):
                return -self.small_heap[0]
            else:
                return self.large_heap[0]
        