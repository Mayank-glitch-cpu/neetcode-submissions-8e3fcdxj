class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols= len(grid),len(grid[0])
        q= deque()  # rotten queue
        visit=set()

        def add_orange(r,c):
            if (r<0 or c<0 or
                r>=rows or c>=cols or
                (r,c) in visit or grid[r][c]==0):
                return
            visit.add((r,c))
            q.append([r,c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append([r,c])
                    visit.add((r,c))

        minute=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=2

                add_orange(r-1,c)
                add_orange(r+1,c)
                add_orange(r,c-1)
                add_orange(r,c+1)
            if q:
                minute+=1 # only update if new oranges were added in the rotten queue
        
        # check for fresh oranges 
        for row in grid:
            if 1 in row:
                return -1
            
        return minute
