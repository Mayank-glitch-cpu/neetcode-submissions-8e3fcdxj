class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res,sol = [] , []

        def dfs():
            if len(sol)==len(nums):
                res.append(sol[:])
                return

            for i in range(len(nums)):
                if nums[i] not in sol:
                    sol.append(nums[i])
                    dfs()
                    sol.pop()
        dfs()
        return res