import numpy as np
class Solution:

    def __init__(self, w: List[int]):
        self.w= w
        self.prob= [0]*len(self.w)
        self.prob[0]= self.w[0]/sum(self.w)
        for i in range(1, len(self.w)):
            self.prob[i] = self.prob[i-1] + self.w[i]/sum(self.w)
        
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