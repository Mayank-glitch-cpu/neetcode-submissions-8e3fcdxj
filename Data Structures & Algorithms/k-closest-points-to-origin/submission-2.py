import heapq
class Solution:

    def dist2origin(self, x,y):
        return (x**2 + y**2)**(0.5)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap= [] # distance with mapping to points

        for point in points:
            # print(point)
            heapq.heappush(heap,(self.dist2origin(point[0], point[1]),point))
        
        res= []

        while heap:
            distance, point= heapq.heappop(heap)
            res.append(point)
            if len(res)>=k:
                return res