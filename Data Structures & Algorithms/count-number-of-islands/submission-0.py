class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res=[]
        curr=[]
        visit=set()
        row,col= len(grid),len(grid[0])
        def dfs(r,c):
            if (r<0 or c<0 or 
                r>=row or c>= col or 
                (r,c) in visit or grid[r][c]=='0'):
                # res.append(curr.copy())
                # print(res)
                return

            curr.append((r,c))
            visit.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        current_island=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] =="1" and (r,c) not in visit:
                    dfs(r,c)
                    current_island+=1
        return current_island

            
