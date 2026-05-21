import heapq
class Solution:
    def distance(self,x,y):
        return ((x**2) + (y**2))**(0.5)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap= []
        out= []
        for point in points:
            dist = self.distance(point[0], point[1])
            heapq.heappush(heap, (dist,point))
        
        while heap:
            distance, point= heapq.heappop(heap)
            out.append(point)
            if len(out)>=k:
                return out