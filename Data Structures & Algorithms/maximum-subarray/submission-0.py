class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, currSum=nums[0],0
        for i in range(len(nums)):
            if currSum<0:
                currSum=0
            currSum += nums[i]
            sum= max(sum,currSum)
        return sum