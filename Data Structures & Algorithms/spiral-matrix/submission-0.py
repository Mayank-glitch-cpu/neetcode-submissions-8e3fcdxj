class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return None
        
        top, bottom= 0, len(matrix)-1
        left, right= 0, len(matrix[0])-1
        out= []
        def dfs_down(j):
            nonlocal top, bottom, left, right # 2. Added nonlocal declarations
            if top > bottom or left > right: return
            while j<=bottom:
                out.append(matrix[j][right])
                j+=1
            right-=1
            dfs_left(right)
        
        def dfs_right(i):
            nonlocal top, bottom, left, right # 2. Added nonlocal declarations
            if top > bottom or left > right: return
            while i<=right:
                out.append(matrix[top][i])
                i+=1
            top+=1
            dfs_down(top)

        def dfs_left(k):
            nonlocal top, bottom, left, right # 2. Added nonlocal declarations
            if top > bottom or left > right: return
            while k>=left:
                out.append(matrix[bottom][k])
                k-=1
            bottom -=1
            dfs_up(bottom)
        
        def dfs_up(l):
            nonlocal top, bottom, left, right # 2. Added nonlocal declarations
            if top > bottom or left > right: return
            while l>=top:
                out.append(matrix[l][left])
                l-=1
            left+=1
            dfs_right(left)
        dfs_right(left)
        return out
