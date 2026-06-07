import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:]= np.array(matrix[::-1]).T
