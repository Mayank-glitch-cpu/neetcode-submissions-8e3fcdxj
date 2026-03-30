import numpy as np
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ########################################
        # brute force :space O(n^2); time O(n^3)
        ######################################## 
        # out=[]
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)+1):
        #         res= np.prod(nums[i:j])
        #         out.append(res)
        # print(out)
        # return int(np.max(out))

        ##########################################
        #optimised solution: time O(n), Space O(1)
        ##########################################
        best= max_here= min_here= nums[0]

        for i  in range(1,len(nums)):
            prev_max= max_here
            prev_min= min_here

            c1= nums[i]
            c2= nums[i]*prev_max
            c3= nums[i]*prev_min

            max_here= max(c1,c2,c3)
            min_here= min(c1,c2,c3)

            if max_here>best:
                best= max_here
        return best