class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s= s[::-1]
        s= s.lstrip()
        res= 0

        for i in range(len(s)):
            if s[i]==' ':
                return res
            res+=1
        return res