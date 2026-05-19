import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix= np.ones(len(nums))
        suffix= np.ones(len(nums))
        for i in range(1,len(nums)):
            prefix[i]= nums[i-1]*prefix[i-1]
        for j in range(len(nums)-2,-1,-1):
            suffix[j] = nums[j+1]*suffix[j+1]
        print(suffix)
        
        out= prefix * suffix
        return [int(num) for num in out]