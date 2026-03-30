class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def find_target(nums,start,end):
            if start > end:
                return False
            
            middle = (start+end)//2

            if nums[middle] == target:
                return True

            if nums[middle] > target:
                return find_target(nums,start,middle-1)

            if nums[middle] < target:
                return find_target(nums,middle+1,end)

        def correct_row(matrix,i):
            n=len(matrix)
            if i>n-1:
                return False

            elif matrix[i][-1] < target:
                return correct_row(matrix,i+1)
                
            else:
                return find_target(matrix[i],0,len(matrix[i])-1)
        
        return correct_row(matrix,0)