class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num=0
        fix_dic= dict.fromkeys(nums,num)
        for n in nums:
            if fix_dic.get(n)==0: # base case if num is not in dictionary 
                fix_dic[n]= num+1
            else:
                return True     
        return False
        
        


         