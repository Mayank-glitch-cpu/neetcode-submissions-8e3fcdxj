import heapq
class Solution:
    def distance(self,points):
        if not points:
            return None 
        x=points[0]
        y=points[1]
        distance= ((0-x)**2+(0-y)**2)**(1/2)
        return distance
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return None
        max_heap=[]
        out=[]
        for point in points:
            distance= self.distance(point)
            heapq.heappush(max_heap,[-distance,point])
            if len(max_heap) >k:
                heapq.heappop(max_heap)[1]

        return [point[1] for point in max_heap ]



        
        

