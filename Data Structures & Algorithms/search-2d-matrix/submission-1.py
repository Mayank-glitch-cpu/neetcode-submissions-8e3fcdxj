class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows= len(matrix)
        cols= len(matrix[0])
        for r in range(rows):
            if matrix[r][-1] < target:
                continue
            else:
                left= 0
                right= cols-1

                while left<=right:
                    m= (left+right)//2

                    if matrix[r][m] < target:
                        left= m+1
                    elif matrix[r][m] > target:
                        right= m -1
                    else:
                        return True
                return False
        return False