class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find_min(nums,start,end):

            middle= (start+end)//2
            print(nums[middle])
            if nums[start]<nums[middle] and nums[middle]<nums[end]:
                return nums[start]
            if nums[start] < nums[middle]:
                return find_min(nums,middle,end)
            if nums[middle]<nums[end]:
                return find_min(nums,start,middle)
            else:
                return min(nums[start],nums[end],nums[middle])

        return find_min(nums,0,len(nums)-1)