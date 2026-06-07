class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        out= []

        while top<= bottom and left<= right:
            # move from left to right
            for i in range(left,right+1):
                out.append(matrix[top][i])
            top+=1
            
            # move from top to bottom
            for j in range(top, bottom+1):
                out.append(matrix[j][right])
            right-=1
            if top<= bottom:

                # move from right to left
                for k in range(right,left-1, -1):
                    out.append(matrix[bottom][k])
                bottom-=1
            
            if left<= right:
                # move from bottom to top
                for l in range(bottom, top-1, -1):
                    out.append(matrix[l][left])
                left+=1
        return out