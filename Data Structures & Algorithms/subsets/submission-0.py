class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        subset=[]
        def dfs(i):

            if i >= len(nums):
                res.append(subset.copy())
                return

            # to include the node 
            subset.append(nums[i])
            dfs(i+1)

            # to not include the node 
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res