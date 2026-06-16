class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res= []

        def backtrack(i, curr, total):
            if total==target:
                copy= curr[:]
                res.append(copy)
                return 

            if i>= len(nums) or total > target:
                return

            curr.append(nums[i])
            # now taking nums[i]
            backtrack(i, curr, total+nums[i])
            #now not taking it
            curr.pop()
            backtrack(i+1, curr, total)

        backtrack(0, [], 0)
        return res