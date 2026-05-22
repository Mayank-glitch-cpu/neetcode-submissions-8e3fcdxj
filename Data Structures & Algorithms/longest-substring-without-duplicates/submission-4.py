class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left= 0
        max_length= 1
        visit= set()
        for right in range(len(s)):
            while s[right] in visit:
                visit.remove(s[left])
                left+=1
            visit.add(s[right])
            max_length= max(max_length, right -left +1)
        return max_length


