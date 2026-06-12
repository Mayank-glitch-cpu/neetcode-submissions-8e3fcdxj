class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = nums[i-1]*prefix[i-1]

        for j in range(len(nums)-2, -1 , -1):
            suffix[j] = nums[j+1]*suffix[j+1]
        print(prefix)
        print(suffix)
        return [a*b for a,b in zip(prefix, suffix)]
