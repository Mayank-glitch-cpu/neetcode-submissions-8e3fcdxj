class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_target(nums,start,end):
            if start > end:
                return -1
            
            middle = (start+end)//2

            if nums[middle] == target:
                return middle

            if nums[middle] > target:
                return find_target(nums,start,middle-1)

            if nums[middle] < target:
                return find_target(nums,middle+1,end)

        return find_target(nums,0,len(nums)-1)       