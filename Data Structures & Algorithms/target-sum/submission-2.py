class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Bottom Up Approach
        dp= [defaultdict(int) for _ in range(len(nums)+1)]
        dp[0][0]= 1 # current index and current sum

        for i in range(len(nums)):
            for curr_sum, count in dp[i].items():
                dp[i+1][curr_sum+nums[i]] +=count
                dp[i+1][curr_sum-nums[i]] += count

        return dp[len(nums)][target]

        # Top Down Approach
        dp= {} # --> memoization

        def backtracking(i,curr_sum):
            if (i,curr_sum) in dp:
                return dp[(i,curr_sum)]

            if i == len(nums):
                return 1 if curr_sum == target else 0

            dp[(i,curr_sum)]= (
                backtracking(i+1,curr_sum + nums[i]) +
                backtracking(i+1, curr_sum - nums[i])
            )

            return dp[(i,curr_sum)]

        return backtracking(0,0)