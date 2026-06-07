class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo= [[-1]* (len(nums) +1) for _ in range(len(nums))]

        def dfs(i,j):
            if i == len(nums):
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            LIS= dfs(i+1, j)  # when we do not include nums[i]

            if j==-1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i+1,i))  # when we include nums[i]
            
            memo[i][j] = LIS
            return LIS

        return dfs(0,-1)