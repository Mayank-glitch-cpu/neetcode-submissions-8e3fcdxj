import numpy as np
class Solution:

    def __init__(self, w: List[int]):
        self.w= w
        self.prob= [0]*len(self.w)
        self.prob[0]= self.w[0]/sum(self.w)
        for i in range(1, len(self.w)):
            self.prob[i] = self.prob[i-1] + self.w[i]/sum(self.w)
        print('weights --->',self.w)
        print('probabilities -->', self.prob)
        
    def pickIndex(self) -> int:
        marker = np.random.uniform(0,1)
        print(marker)
        running_sum= 0
        l,r = 0, len(self.prob)-1
    
        while l<r:
            m=(l+r)//2
            if self.prob[m] <= marker:
                l= m +1
            else:
                r= m 
        return l
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()