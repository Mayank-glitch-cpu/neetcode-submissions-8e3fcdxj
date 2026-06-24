class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = min_here = max_here = nums[0]

        for i in range(1,len(nums)):
            prev_min= min_here
            prev_max= max_here

            c1 = nums[i]
            c2 = nums[i]*prev_min
            c3 = nums[i]*prev_max

            max_here= max(c1,c2,c3)
            min_here= min(c1,c2,c3)

            if best< max_here:
                best= max_here

        return best 