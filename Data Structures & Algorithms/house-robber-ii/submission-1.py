class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        nums1= [n for n in nums[:len(nums)-1]]
        nums2= [n  for n in nums[1:]]
        # print(nums1)
        # print(nums2)
        rob1, rob2= 0,0
        for n in nums1:
            temp= max(rob1+n, rob2)
            rob1= rob2
            rob2= temp
        res1= rob2
        # print(res1)
        rob1,rob2=0,0
        for n in nums2:
            temp= max(rob1+n, rob2)
            rob1= rob2
            rob2= temp
        res2= rob2
        # print(res2)
        return max(res1,res2)