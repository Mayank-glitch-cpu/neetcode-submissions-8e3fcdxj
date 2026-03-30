class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n= set()
        for num in nums:
            if num in n:
                return True
            n.add(num)
        return False
