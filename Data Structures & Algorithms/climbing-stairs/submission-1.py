class Solution:
    def climbStairs(self, n: int) -> int:
        current , prev = 1, 1 
        for i in range(n-1):
            temp= current
            current += prev
            prev = temp
        return current 