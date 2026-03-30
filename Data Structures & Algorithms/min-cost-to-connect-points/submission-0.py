class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n= len(points)
        res=0
        min_heap= [(0,0)] # cost, index

        visit= set()

        while len(visit)<n:
            cost,i= heapq.heappop(min_heap)
            if i in visit:
                continue
            res+=cost
            visit.add(i)

            for j in range(n):
                if j not in visit:
                    x1,y1= points[i]
                    x2,y2= points[j]
                    dist= abs(x2-x1) + abs(y2-y1)
                    heapq.heappush(min_heap,(dist,j))
        
        return res

            