class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap= []
        heapq.heappush(minHeap, [0,0])
        totalSum= 0
        trajectory = []
        visit= set()

        while minHeap:
            dist , index = heapq.heappop(minHeap)

            if index in visit:
                continue 

            visit.add(index)
            totalSum += dist
            trajectory.append(points[index])

            for nei in range(len(points)):
                if nei not in visit:
                    dst= abs(points[index][0]- points[nei][0]) + abs(points[index][1] - points[nei][1])
                    # print(dst)
                    heapq.heappush(minHeap,[dst, nei])

        print('For this trajectory --> ', trajectory, 'total sum =',totalSum)
        return totalSum