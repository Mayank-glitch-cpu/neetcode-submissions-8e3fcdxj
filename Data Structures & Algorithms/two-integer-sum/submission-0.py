class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffmap={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in diffmap:
                return [diffmap[diff] , i] 
            else:
                diffmap[num]=i
        print("hash map",diffmap)
