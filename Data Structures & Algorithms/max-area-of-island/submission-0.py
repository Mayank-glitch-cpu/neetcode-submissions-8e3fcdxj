class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit=set()
        row,col= len(grid),len(grid[0])

        def dfs(r,c):
            if (r<0 or c<0 or 
                r>=row or c>= col or 
                (r,c) in visit or grid[r][c]== 0):
                return 0
            
            visit.add((r,c))
            area=1
            area+=dfs(r-1,c)
            area+=dfs(r+1,c)
            area+=dfs(r,c-1)
            area+=dfs(r,c+1)
            return area
        max_area=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] ==1 and (r,c) not in visit:
                    max_area=max(max_area,dfs(r,c))
        return max_area