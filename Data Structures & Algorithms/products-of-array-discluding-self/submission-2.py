class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum, suffix_sum= [1]*len(nums), [1]*len(nums)
        prefix_sum[0], suffix_sum[-1]=1, 1

        for i in range(1,len(nums)):
            prefix_sum[i] = prefix_sum[i-1]*nums[i-1]

        for j in range(len(nums)-2,-1,-1):
            suffix_sum[j] = suffix_sum[j+1]*nums[j+1]

        return [a*b for a,b in zip(prefix_sum, suffix_sum)]