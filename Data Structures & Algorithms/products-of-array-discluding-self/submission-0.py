class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # i will do it with a prefic and suffix algo
        prefix=1 
        n= len(nums)
        output=[1]*n
        for i in range(n):
            output[i] *= prefix
            prefix*= nums[i]
        # So, till this point the output array has the product before each index i 

        # So now i will calculate the product of all elements after index i (from right to left)

        suffix=1
        for i in range(n-1,-1,-1):
            output[i]*= suffix
            suffix*= nums[i]
        # print(output)
        return output
