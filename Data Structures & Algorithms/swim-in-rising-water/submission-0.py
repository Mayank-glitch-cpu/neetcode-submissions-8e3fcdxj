class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visit= set()
        N= len(grid)
        minH= [[grid[0][0],0,0]]
        directions= [[0,1],[0,-1],[1,0],[-1,0]]

        visit.add((0,0))

        while minH:

            t,r,c= heapq.heappop(minH)
            if r== N-1 and c==N-1:
                return t

            for dr, dc in directions:
                nR,nC= r+ dr, c+dc
                if (nR<0 or nC<0 or nR==N or nC==N or (nR,nC) in visit):
                    continue
                visit.add((nR,nC))
                heapq.heappush(minH,[max(t,grid[nR][nC]),nR,nC])