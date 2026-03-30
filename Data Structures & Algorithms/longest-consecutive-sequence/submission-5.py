class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lgt=0
        length=[]
        LIS=[]

        nums.sort()
        print('Sorted nums',nums)
        nums_set={i for i in nums}
        nums=sorted(nums_set)
        print(nums)

        if len(nums)==1:
            return 1
        if len(nums)==0:
            return 0
        for i in range(1,len(nums_set)):
            if  nums[i]-nums[i-1]==1:
                LIS.append(nums[i-1])
                lgt+=1
                print('LIS',LIS)
                print(f'Length of LIS at ',i,lgt)
            else:
                length.append(lgt)
                print('length when it broke',lgt)
                lgt=0
                LIS=[]
            length.append(lgt)

        return max(length)+1