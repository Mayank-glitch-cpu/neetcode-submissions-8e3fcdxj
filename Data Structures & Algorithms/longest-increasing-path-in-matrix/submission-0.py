class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0 
        rows,cols= len(matrix), len(matrix[0])

        dp= [[0]*cols for _ in range(rows)]

        def dfs(r,c):
            if dp[r][c]!=0:
                return dp[r][c]
            res=1
            dir= [(0,1),(0,-1),(1,0),(-1,0)]
            for dr,dc in dir:
                nr,nc= r+dr, c+dc
                if (0<=nr<rows and 
                    0<=nc<cols and 
                    matrix[nr][nc]> matrix[r][c]):
                    res= max(res,1+dfs(nr,nc))
            dp[r][c]= res
            return res

        max_len= 0
        for r in range(rows):
            for c in range(cols):
                max_len= max(max_len, dfs(r,c))

        return max_len