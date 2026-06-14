class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l<= r:
            m = (l + r)//2
            print(m)
            if ((m-1<0 or nums[m]!=nums[m-1]) and (m+1 == len(nums) or nums[m]!=nums[m+1])):
                return nums[m]

            leftside = m-1 if (m-1) >=0 and nums[m-1] == nums[m] else m
            
            if leftside % 2 ==0:
                l = m+1
            else:
                r= m-1