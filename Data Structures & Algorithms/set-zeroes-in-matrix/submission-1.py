class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols= len(matrix), len(matrix[0])
        zero_row= set()
        zero_col= set()

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    zero_row.add(r)
                    zero_col.add(c)

        for r in range(rows):
            for c in range(cols):
                if r in zero_row or c in zero_col:
                    matrix[r][c]=0