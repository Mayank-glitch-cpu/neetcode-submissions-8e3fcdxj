import numpy as np
class Solution:

    def __init__(self, w: List[int]):
        self.w= w
        self.prob= [w[i]/sum(w) for i in range(len(w))]

    def pickIndex(self) -> int:
        marker = np.random.uniform(0,1)
        running_sum= 0
        for index , prob in enumerate(self.prob):
            running_sum += prob

            if running_sum >= marker:
                return index

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()