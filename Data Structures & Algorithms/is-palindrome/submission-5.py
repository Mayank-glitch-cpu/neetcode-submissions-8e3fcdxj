class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = (re.sub(r"[^a-zA-Z0-9]","",s)).lower()
        l, r = 0, len(cleaned) -1
        print(cleaned)
        while l <= r:
            if cleaned[l] != cleaned[r]:
                return False
            l+=1
            r-=1
        return True
         