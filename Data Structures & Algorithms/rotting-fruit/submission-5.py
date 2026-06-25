class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        rows, cols= len(grid), len(grid[0])
        q= deque()
        visit=set()
        def dfs(r,c):
            # this function will make the nearby oranges rot
            if (r<0 or c<0 or
                r>=rows or c>=cols or
                (r,c) in visit or grid[r][c]==0):
                return
            visit.add((r,c))
            q.append((r,c))

        # lets find the rotten index
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    visit.add((r,c))
                    q.append((r,c))

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c]=2
                dfs(r-1,c)
                dfs(r+1,c)
                dfs(r,c-1)
                dfs(r,c+1)
            if q:
                time+=1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    return -1
        return time