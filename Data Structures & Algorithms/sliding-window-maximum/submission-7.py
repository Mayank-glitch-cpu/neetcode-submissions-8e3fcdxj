class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k> len(nums):
            return list(max(nums))
        if len(nums)==1:
            return nums
        left =0 
        right=k
        out=[]
        while right<=len(nums):
            out.append(max(i for i in nums[left:right]))
            left+=1
            right+=1
        return out

