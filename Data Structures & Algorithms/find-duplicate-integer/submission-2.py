class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)

        if not nums:
            return None

        if len(nums)<=2:
            if nums[0]==nums[1]:
                return nums[0]
            else:
                return None

        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return nums[i]
        
        return None